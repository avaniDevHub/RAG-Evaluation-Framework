const API_BASE = "http://127.0.0.1:8000";

export async function evaluateRAG(question) {
  const res = await fetch(`${API_BASE}/evaluate`, {
    method: "POST",
    headers: {
      "Content-Type": "application/json"
    },
    body: JSON.stringify({ question })
  });

  if (!res.ok) {
    throw new Error("Backend error");
  }

  return res.json();
}
