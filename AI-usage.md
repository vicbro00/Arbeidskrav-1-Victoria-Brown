AI som ble brukt i dette arbeidskravet var for det meste Claude.ai, med litt bruk av ChatGPT.

## Prompt 1:
Oppgave 2.

Min prompt:
if choice == "1":
    print("Register a new session")
    new_session = {
        "topic": input("What is the session topic? ").capitalize(),
        "duration_minutes": int(input("How long is the session? ")),
        "status": input("Planned or completed? ").capitalize()
    }
    all_sessions.append(new_session)
    print(new_session)
What i have is this code where the user can register a new study session. But i need conditionals so that the user 
cannot input anything invalid, such as empty strings, strings in duration minutes, or something other than "planned" 
or "completed". 
Im not sure how i can add conditionals to the list of dictionaries. 
Do not give me any code, just help me understand how i can restructure my code so that the user cannot input anything invalid.

### Svar:
Good instinct to want validation here — right now your code trusts the user completely, and it'll crash or store garbage
the moment someone types "abc" for duration or hits enter with nothing.

Here's the concept you're missing: validate before you store, not after. Right now you're doing input → immediately 
shove into dictionary. Instead, you want: input → check if it's valid → if not, ask again → only once it's valid, use it.

That naturally leads to a while loop pattern for each field, something like:

Keep asking for the topic until the string isn't empty
Keep asking for duration until what they typed can actually convert to a number
Keep asking for status until it matches "Planned" or "Completed"

Let's break down each one conceptually:

1. Empty string check (topic)
An empty string is falsy in Python, so you can loop while the input, after stripping whitespace, is empty. 
2. The .strip() matters here — someone typing just spaces would otherwise sneak past a plain emptiness check.

Numbers only (duration)
The tricky part is that input() always gives you a string, and int() will crash (raise an exception) 
if it's not a valid number — it won't just return False. So this isn't a simple condition check, 
it's a case for try/except: try to convert it, and if it fails, catch the error and ask again. 
This is a different structural tool than an if-statement, which is likely part of why it feels hard to fit in — 
a plain conditional can't test "would this crash if I converted it."

3. Restricted values (status)
This one's a straightforward membership check — you want to keep looping while the input, after .capitalize(), 
is not one of your two allowed values. Conceptually: "keep asking until the answer is in my allowed list."

Putting it together structurally:
Instead of one input() line per field feeding directly into the dictionary, you'd have three separate small loops 
before the dictionary is built — each loop's only job is to produce one clean, valid variable (like topic, duration, status). 
Only after all three loops finish do you build new_session from those already-validated variables.

Does that reshape make sense as a plan? If you want, try writing just the empty-string loop for topic first, 
and I can tell you if the logic holds before you move to the trickier try/except one for duration.

