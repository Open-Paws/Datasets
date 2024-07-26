# Synthetic Seed Data

## Overview

This folder contains a CSV file titled `Multilingual Vegan Questions` which serves as seed data for initiating the collection of conversation responses for human feedback. The primary purpose of this data is to facilitate interactions where users from various language backgrounds can participate in dialogues, taking turns responding as the AI or the human. These dialogues can then be ranked by the same volunteers for their impact on animals.

## File Description

### Multilingual Vegan Questions

The `Multilingual Vegan Questions.csv` file includes two columns:

- **Questions**: This column contains a variety of questions related to veganism, designed to prompt discussion and responses.
- **Languages**: This column indicates the language of the corresponding question, enabling multilingual interaction. The language is written first within its own script or alphabet, then the English name for the language is provided in brackets.

### CSV Structure

The CSV file is structured as follows:

| Questions | Languages |
|-----------|-----------|
| [Vegan question 1] | [Language 1] |
| [Vegan question 2] | [Language 2] |
| ... | ... |

## Usage

This seed data is intended to be used in conversation collection platforms where users engage in dialogue exchanges. The goal is to gather diverse responses, enhancing the training of AI models through human feedback. Users can select questions in their preferred language and respond either as the AI or as the human participant in the conversation.

### Steps to Use

1. **Load the CSV**: Import the `Multilingual Vegan Questions.csv` file into your labelling platform (see the [Human-Feedback-Label-Studio](https://github.com/Open-Paws/Human-Feedback-Label-Studio) repo for our implementation of Label Studio)
2. **Select a Question**: Choose a question from the `Questions` column.
3. **Respond**: Users take turns responding to the selected question, alternating roles between AI and human.
4. **Collect Feedback**: Gather responses to use as training data for AI models, improving their ability to handle multilingual interactions.

## Contribution

If you wish to contribute additional questions or languages to this seed data, please follow these steps:

1. **Add Questions**: Insert new questions into the `Questions` column.
2. **Specify Languages**: Ensure the corresponding languages are accurately represented in the `Languages` column.
3. **Submit**: Update the `Multilingual Vegan Questions.csv` file and submit a pull request or share the updated file with the project maintainers.

## Language Selection

There are more than [7,000 officially recognised living languages]([## License](https://www.ethnologue.com/)) and unfortunately due to resource constraints, we don't have the capacity or knowledge required to cover all of them. We therefore selected the languages that we believe we are most likely to find relevant data in and/or find volunteers to help us collect and rank data in.

However, we welcome all languages with open arms and would love to further expand the range of languages we are able to cover. If you speak a language that is not already listed, please [contact us through the submission form on our website](https://www.openpaws.ai/get-involved) with more details so we can work together to ensure your language is added to the project.

## License

This data is provided under an open license, allowing for free use and modification. By contributing, you agree to share your additions under the same terms.

For any questions or further information, please contact the project maintainers.
