# 💭 Reflection: Game Glitch Investigator

Answer each question in 3 to 5 sentences. Be specific and honest about what actually happened while you worked. This is about your process, not trying to sound perfect.

## 1. What was broken when you started?

- What did the game look like the first time you ran it?
* It looked like I was about to go to an actaul game after looking at the landing page but it turns out that was the game.
- List at least two concrete bugs you noticed at the start  
  (for example: "the secret number kept changing" or "the hints were backwards").
* The hints were backwards
* The new game button doesn't work
* Pressing enter/return doesn't work once the number is added
* Less chances to try on easy than advertised. It says 20 but you only have 5
* guessing too high on even attempts gives you bonus points instead of penalizing you
---

## 2. How did you use AI as a teammate?

- Which AI tools did you use on this project (for example: ChatGPT, Gemini, Copilot)? Claude
- Give one example of an AI suggestion that was correct (including what the AI suggested and how you verified the result). 
* Wrong hints was one of the suggestions the AI gave. I verified it by running the guessing game and noticed the hints tell you the opposite of what is helpful
- Give one example of an AI suggestion that was incorrect or misleading (including what the AI suggested and how you verified the result).
* I noticed it said that "on every 2nd guess, the secret number is converted to a string internally, making it nearly impossible to win on those attempts" which I thought was incorrect because I was able to win while I was on the 2nd guess.
---

## 3. Debugging and testing your fixes

- How did you decide whether a bug was really fixed? I tested them on the browser and saw the issue was really not happening any more
- Describe at least one test you ran (manual or using pytest)  
  and what it showed you about your code.
  I ran pytest on test_game_logic.py which had two tests specifically for the hint bug: test_too_high_message_says_go_lower and test_too_low_message_says_go_higher. Before the fix those tests would have failed because the game was telling you to go higher when your guess was already too high. Running them after the fix showed all 9 tests passing, which confirmed the hints were finally pointing the right way. It was useful because the tests caught the exact line that was wrong instead of me just guessing by clicking around in the browser.
- Did AI help you design or understand any tests? How?
Yeah, Claude helped a lot with the tests. I told it the hint bug I found and it wrote two pytest functions. test_too_high_message_says_go_lower and test_too_low_message_says_go_higher that checked the actual message text, not just whether the outcome said "Too High" or "Too Low." It also pointed out that the original tests would crash because check_guess returns two values and the tests were only expecting one, which I wouldn't have caught on my own right away.
---

## 4. What did you learn about Streamlit and state?

- In your own words, explain why the secret number kept changing in the original app.
- How would you explain Streamlit "reruns" and session state to a friend who has never used Streamlit?
- What change did you make that finally gave the game a stable secret number?

---

## 5. Looking ahead: your developer habits

- What is one habit or strategy from this project that you want to reuse in future labs or projects?
  - This could be a testing habit, a prompting strategy, or a way you used Git.
- What is one thing you would do differently next time you work with AI on a coding task?
- In one or two sentences, describe how this project changed the way you think about AI generated code.
