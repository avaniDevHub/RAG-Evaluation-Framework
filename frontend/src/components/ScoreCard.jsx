export default function ScoreCard({ label, value }) {
  return (
    <div style={{
      border: "1px solid #ccc",
      padding: 20,
      width: 150,
      textAlign: "center"
    }}>
      <h3>{label}</h3>
      <strong>{value}</strong>
    </div>
  );
}
