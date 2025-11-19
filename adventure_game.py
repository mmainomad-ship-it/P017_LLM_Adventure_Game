# adventure_game.py
# STEP 1: Import the necessary library and initialize the Ollama client.
import ollama  # Import the ollama library to interact with the local LLM

client = ollama.Client(
    host="http://localhost:11434"
)  # Initialize the Ollama client connection to the default host/port

# STEP 2: Define the game state variables and the local LLM model to use.
current_location = (
    "A dark forest path"  # Global state variable tracking where the player is
)
LLM_MODEL = "llama3"  # Define the name of the model you have pulled with Ollama


# STEP 4: Implement the core logic for the LLM call, ensuring the prompt forces a structured response.
def get_llm_response(location: str, choice: str) -> str:
    """Generates the story resolution and new location based on current state and player choice."""
    prompt = (  # Construct the prompt detailing the current state and expected output format
        f"The player is currently at: {location}. "
        f"They chose action number {choice}. Describe the outcome of this action "
        "and name the **NEW** location they arrive at. Start your response with the NEW location name on its own line."
    )
    # Call the local LLM and return the generated text
    response = client.generate(model=LLM_MODEL, prompt=prompt)
    return response["response"]


# STEP 5a: Initial Scenario - Generate the first story description and choices.
if __name__ == "__main__":
    print("--- 🗺️ STARTING THE ADVENTURE ---")
    # Prompt the LLM for the initial scenario and actions (1, 2, 3)
    initial_prompt = "Describe a starting location for a fantasy adventure, and list exactly three possible actions (1, 2, 3) the player can take."
    # STEP 5b: Call LLM, print results, and start the main game loop.
    initial_response = client.generate(model=LLM_MODEL, prompt=initial_prompt)[
        "response"
    ]
    print("\n" + initial_response + "\n")

    # --- Main Game Loop ---
    while (
        True
    ):  # The game continues until the player (or the LLM response) forces an exit
        # STEP 5c: Get user input, call LLM, parse output, and update state.
        choice = input(
            f"Enter your choice (1, 2, 3) from your current location '{current_location}': "
        )

        # Check for exit condition (simple 'quit')
        if choice.lower() in ["q", "quit"]:
            print("Adventure ended. Farewell!")
            break

        llm_output = get_llm_response(
            current_location, choice
        )  # Call the LLM with current state and choice

        # The LLM's response is structured: new location name is always on the first line.
        try:
            new_location, story_description = llm_output.split("\n", 1)
        except ValueError:
            new_location = "Unknown Fate"
            story_description = llm_output
            print(
                "\n[Game Error: LLM did not provide a structured response. Game state may be unstable.]"
            )

        current_location = new_location.strip()  # Update the global game state
        print("\n--- You travel onward ---")
        print(f"**NEW LOCATION:** {current_location}")
        print("-" * 30)
        print(
            story_description.strip()
        )  # Print the narrative description of the outcome
        print("-" * 30)
