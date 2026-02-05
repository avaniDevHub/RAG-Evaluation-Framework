import { useState } from "react";
import { Button, Stack, Typography } from "@mui/material";
import ScoreCard from "../components/ScoreCard";
import Charts from "../components/Charts";
import { evaluateRAG } from "../api";

const Dashboard = () => {
  const [result, setResult] = useState(null);

  const runEvaluation = async () => {
    const payload = {
      question: "How do I reset my password?",
      search_results: [
        {
          document_id: "doc1",
          content: "To reset your password, go to settings.",
          relevant: true
        },
        {
          document_id: "doc2",
          content: "Company history info.",
          relevant: false
        }
      ],
      answer: "You can reset your password from the settings page."
    };

    const response = await evaluateRAG(payload);
    setResult(response.data);
  };

  const chartData = result
    ? [
        { metric: "Faithfulness", score: result.answer_quality.faithfulness },
        { metric: "Relevance", score: result.answer_quality.relevance },
        { metric: "Completeness", score: result.answer_quality.completeness }
      ]
    : [];

  return (
    <Stack spacing={4} alignItems="center" mt={4}>
      <Typography variant="h4">
        RAG Evaluation Dashboard
      </Typography>

      <Button variant="contained" onClick={runEvaluation}>
        Run Evaluation
      </Button>

      {result && (
        <>
          <Stack direction="row" spacing={3}>
            <ScoreCard
              title="Hit Rate"
              value={result.search_quality.hit_rate}
            />
            <ScoreCard
              title="Precision@5"
              value={`${result.search_quality["precision@5"]}%`}
            />
          </Stack>

          <Charts data={chartData} />
        </>
      )}
    </Stack>
  );
};

export default Dashboard;