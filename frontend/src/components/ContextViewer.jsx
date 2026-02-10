export default function ContextViewer({ contexts }) {
  return (
    <ul>
      {contexts.map((ctx, i) => (
        <li key={i} style={{ marginBottom: 10 }}>
          <pre>{ctx.content}</pre>
          <small>{ctx.source}</small>
        </li>
      ))}
    </ul>
  );
}
