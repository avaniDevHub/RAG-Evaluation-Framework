export default function FailureBadge({ reason }) {
  const colors = {
    retrieval_failure: "red",
    generation_failure: "orange",
    pass: "green"
  };

  return (
    <div style={{
      background: colors[reason],
      color: "white",
      padding: "8px 16px",
      display: "inline-block",
      marginTop: 10
    }}>
      {reason.replace("_", " ").toUpperCase()}
    </div>
  );
}
