import axios from "axios";

const API = axios.create({
  baseURL: "http://localhost:8000"
});

export const evaluateRAG = async (payload) => {
  return await API.post("/evaluate", payload);
};
