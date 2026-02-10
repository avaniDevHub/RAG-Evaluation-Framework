import { useState } from "react";
import { evaluateRAG } from "../api";
import ScoreCard from "../components/ScoreCard";
import ContextViewer from "../components/ContextViewer";
import FailureBadge from "../components/FailureBadge";

export default function Dashboard() {
  const [question, setQuestion] = useState("");
  const [result, setResult] = useState(null);
  const [loading, setLoading] = useState(false);

  const runEvaluation = async () => {
    setLoading(true);
    try {
      const data = await evaluateRAG(question);
      setResult(data);
    } catch (e) {
      alert("Evaluation failed");
    }
    setLoading(false);
  };

  return (
    <div style={{ padding: 30, maxWidth: "1200px", margin: "0 auto" }}>


      <h1>RAG Evaluation Dashboard</h1>

      <input
        value={question}
        onChange={(e) => setQuestion(e.target.value)}
        placeholder="Enter your question"
        style={{ width: "100%", padding: 10 }}
      />

      <button onClick={runEvaluation} disabled={loading}>
        {loading ? "Evaluating..." : "Run Evaluation"}
      </button>

      {result && (
        <>
          <h2>Generated Answer</h2>
          <div
  style={{
    background: "#f9f9f9",
    padding: "20px 24px",
    borderRadius: 10,
    lineHeight: 1.7,
    whiteSpace: "pre-wrap",
    wordBreak: "break-word",
    width: "100%",
  }}
>
  {result.answer}
</div>
          <FailureBadge reason={result.metrics.failure_reason} />

          <h2>Metrics</h2>
          <div
          style={{
          display: "flex",
          gap: 20,
          flexWrap: "wrap",}}
          >

            <ScoreCard label="Hit Rate" value={result.metrics.hit_rate} />
            <ScoreCard label="Precision@k" value={result.metrics["precision@k"]} />
            <ScoreCard label="Faithfulness" value={result.metrics.faithfulness} />
          </div>

          <h2>Retrieved Contexts</h2>
          <ContextViewer contexts={result.retrieved_chunks} />
        </>
      )}
    </div>
  );
}
