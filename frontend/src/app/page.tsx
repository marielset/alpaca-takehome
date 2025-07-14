"use client";
import React, { useState } from "react";

export default function Home() {
  const [sessionNotes, setSessionNotes] = useState("");
  const [hasGeneratedResponse, setHasGeneratedResponse] =
    useState<boolean>(false);
  const [loading, setLoading] = useState(false);

  const handleSubmit = async (e: React.FormEvent) => {
    e.preventDefault();
    setLoading(true);

    const form = e.currentTarget as HTMLFormElement;
    const formData = new FormData(form);

    try {
      const response = await fetch(
        `${process.env.NEXT_PUBLIC_API_URL}/generate-note`,
        {
          method: "POST",
          body: formData,
        }
      );

      const data = await response.json();
      setHasGeneratedResponse(true);
      setSessionNotes(data.note);
    } catch (err) {
      console.error("Error generating note:", err);
    } finally {
      setLoading(false);
    }
  };

  const handleSave = async () => {
    const formData = new FormData();
    formData.append("note", sessionNotes);

    try {
      const response = await fetch(
        `${process.env.NEXT_PUBLIC_API_URL}/save-note`,
        {
          method: "POST",
          body: formData,
        }
      );

      const data = await response.json();
      console.log(data);
      console.log("Saved note with ID:", data.id);
    } catch (error) {
      console.error("Error saving note:", error);
    }
  };

  return (
    <div className="max-w-2xl mx-auto p-6">
      <h1 className="text-2xl font-semibold mb-4">Therapy Note Generator</h1>
      <form onSubmit={handleSubmit} className="space-y-4">
        <label className="block font-medium">Session Notes:</label>
        <textarea
          rows={10}
          name="text"
          className="w-full text-black border border-gray-300 p-3 rounded resize-y"
          placeholder={"Please write your notes here."}
          value={sessionNotes}
          onChange={(e) => setSessionNotes(e.target.value)}
        />
        <div className="flex justify-between">
          <button
            type="submit"
            disabled={loading}
            className="bg-blue-600 text-white px-4 py-2 rounded hover:bg-blue-700"
          >
            {loading
              ? "Generating..."
              : hasGeneratedResponse
              ? "Regenerate Note"
              : "Generate Note"}
          </button>
          {hasGeneratedResponse && (
            <button
              type="button"
              onClick={handleSave}
              className="bg-green-600 text-white px-4 py-2 rounded hover:bg-green-700"
            >
              Save
            </button>
          )}
        </div>
      </form>
    </div>
  );
}
