# Mariel Setton's Alpaca Health Software Engineering Take-Home Project

### - Approach and challenge

I thought about this from a user perspective first- what does the user want and need to see, what would complicate the application. Time was the biggest challenge, so I had to make sure I had enough time to get through the important features.

### - Design decisions

My first step was to consider what the core functionality was and get started on that. The therapist wants to write notes in a text window and see the formatted output from AI. Should we want therapists to be able to see their original notes, we can return those in the response as well and display them in a separate window.

I wanted to allow for regeneration of AI notes based on edits, and then once the user is satisfied, they are able to save notes to their database.

I deprioritized allowing different users, as that would only make sense with login functionality.

With more time, I would have added the ability to save details about the session in their own distinct variables such as session length, session type, and other fields. Those would go in the form I created as separate fields. I would also consider allowing the therapist to edit the prompt to AI. That might end up being distracting though since without proper knowledge, they might end up misusing the prompt section and conflate it with the notes section.

### - Assumptions

Therapists do not need to see their original notes once they are submitted.

### - Sources

I used AI to generate code snippets and help me think through pros and cons of database decisions since I'm most comfortable with a typescript backend.
AI wrote the schemas module- whereas I would usually add a types module in node.js
