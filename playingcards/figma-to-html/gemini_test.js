const { GoogleGenerativeAI } = require("@google/generative-ai");
const genAI = new GoogleGenerativeAI("AIzaSyAFxbn2ZgZSRG7k3T2Bnze74eAVt3xN4RE");
async function run() {
// For text-only input, use the gemini-pro model
const model = genAI.getGenerativeModel({ model: "gemini-pro"});
const prompt = "Create a one sentence action move for a character, similar to a pokemon card. Start the sentence with a blank for the user. "
const result = await model.generateContent(prompt);
const response = await result.response;
const text = response.text();
console.log(text);
}
run();

