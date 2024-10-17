# Quantitative-Analysis-of-ChatGPT-s-Efficacy-in-Software-Debugging-Prompts
Quantitative Analysis of ChatGPT's Efficacy in Software Debugging Prompts

This project entails a comprehensive analysis of ChatGPT's efficiency in addressing software debugging prompts. Utilizing a rich dataset from DevGPT, including GitHub issues, commits, and discussion sections, the study uncovers extensive usage of ChatGPT in software debugging contexts. We execute sentiment analysis on issue descriptions, revealing insights into the emotional tone of these interactions. Additionally, the project calculates the average resolution times across various programming languages, highlighting the differences in debugging complexities. The correlation between resolution times and programming languages is also explored, providing valuable metrics on how programming language complexity impacts debugging efficacy. This analysis offers a nuanced understanding of ChatGPT's role and effectiveness in software debugging, serving as a critical resource for developers and researchers in AI-enhanced programming environments and further help in enhancing future versions of ChatGPT.

Dataset and Project Link:
https://drive.google.com/file/d/1TvWMn0F8G2uDnMrNpz5wuL8RV-85QldG/view?usp=drive_link

Dataset Description:
https://github.com/NAIST-SE/DevGPT/blob/main/DevGPT_Link_Sharing_Preprint.pdf

Findings:
1. Generic Queries in Debugging: ChatGPT’s initial responses were often too broad, making bug identification slower. Developers had to manually refine queries due to the lack of targeted follow-up questions, which could have improved efficiency.

2. Impact on Bug Localization: The absence of specific, relevant follow-ups resulted in longer times to identify and resolve bugs. More tailored interactions could have significantly sped up the process.

3. Resolution Time Variations: Bug resolution times varied across languages, ranging from 1 to 56 days, depending on error complexity. This highlighted ChatGPT’s difficulty in addressing complex issues with generic responses.

Dynamic Prompt Engineering Prototype:
1. Single-Turn Interactions: The prototype improved ChatGPT’s responses by making them more relevant and focused on the specific issue at hand, reducing the need for additional clarifications.

2. Multi-Turn Interactions: In multi-turn dialogues, the prototype refined each follow-up question, maintaining context and delivering progressively more precise responses, which enhanced debugging efficiency.

3. Impact: By generating more targeted follow-up queries, the prototype reduced bug localization and resolution time, making interactions more efficient.


