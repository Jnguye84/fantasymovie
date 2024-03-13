// mainModule.js
import { GoogleGenerativeAI } from "@google/generative-ai";
const API_KEY = "AIzaSyAFxbn2ZgZSRG7k3T2Bnze74eAVt3xN4RE";
const genAI = new GoogleGenerativeAI(API_KEY);
const model = genAI.getGenerativeModel({ model: "gemini-pro" });

async function run() {
    const prompt = "Create a one sentence action move for a character, similar to a pokemon card. Start the sentence with a blank for the user. "
    const result = await model.generateContent(prompt);
    const response = await result.response;
    const text = response.text();
    console.log(text); //chatGPT
}
const result = run();
export { result  };