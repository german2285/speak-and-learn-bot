# Speak-and-Learn Bot

Speak-and-Learn Bot is an interactive bot designed to facilitate language learning through conversation. It connects to a server and starts up, ready for interaction.

## Features

- **Main Menu**: Upon receiving the "Start" command, the bot sends the user a main menu with buttons for "Profile", "Search", and "Settings".
- **User Matching**: When the user selects "Search", the bot finds another user and randomly assigns roles: one user will describe a topic, and the other will guess.
- **Topic and Keywords**: The user who describes receives a topic, while the guessing user gets a list of keywords (2 correct and 8 incorrect).
- **Keyword Selection**: The guessing user selects keywords, and the bot checks them for correctness, sending the results to both users.
- **Statistics and Difficulty**: The bot updates statistics and calculates a difficulty coefficient based on the results.
- **Chat Status**: After the conversation, the bot updates the chat status and notifies the users.

## Getting Started

To start using the Speak-and-Learn Bot, simply connect it to the server and issue the "Start" command.

## Commands

- **Start**: Initiates the main menu.
- **Profile**: Access user profile settings.
- **Search**: Find another user for a conversation.
- **Settings**: Adjust bot settings.

## How It Works

1. **Initialization**: The bot connects to the server and becomes ready for interaction.
2. **Main Menu**: Users can navigate through the main menu to access different features.
3. **User Matching**: The bot pairs users and assigns roles.
4. **Conversation**: One user describes a topic, and the other guesses using provided keywords.
5. **Results and Statistics**: The bot evaluates the guesses, updates statistics, and calculates difficulty.
6. **Completion**: The bot updates the chat status and notifies users of the results.

Enjoy learning with Speak-and-Learn Bot!