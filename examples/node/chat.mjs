// Chat completion through FastAIToken with the official OpenAI SDK.
//
//   npm install openai
//   export FASTAITOKEN_API_KEY=sk-...
//   export FASTAITOKEN_BASE_URL=...   # copy from the FastAIToken console
//   node examples/node/chat.mjs "你好"
import OpenAI from "openai";

const apiKey = process.env.FASTAITOKEN_API_KEY;
const baseURL = process.env.FASTAITOKEN_BASE_URL;
if (!apiKey || !baseURL) {
  console.error("Set FASTAITOKEN_API_KEY and FASTAITOKEN_BASE_URL (see the FastAIToken console).");
  process.exit(1);
}

const client = new OpenAI({ apiKey, baseURL });
const model = process.env.FASTAITOKEN_MODEL ?? "gpt-5.5";
const prompt = process.argv.slice(2).join(" ") || "Hello!";

const stream = await client.chat.completions.create({
  model,
  messages: [{ role: "user", content: prompt }],
  stream: true,
});
for await (const chunk of stream) {
  process.stdout.write(chunk.choices[0]?.delta?.content ?? "");
}
process.stdout.write("\n");
