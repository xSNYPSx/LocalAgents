# LocalAgents
These agents work based on any local model.
You ask your question and simply indicate the number of agents and experts who will answer it.
For example, you indicated 10 agents.
First, 10 agents will express their opinion on your question regardless of each other's answers. Then the other 10 expert agents will leave comments on the answers of the first ten. Experts take turns leaving a comment and seeing comments from other experts. In the end, the super expert draws up a final answer based on all the conclusions.


For this to work, first launch Lm Studio and turn on the server. Please specify port 1263 in LM Studio for the script to work.
You will also need any local model, microsoft phi-2 is the fastest, but you can try something more powerful, on average the response takes from 10 minutes to 30 minutes, depending on the number of agents and the speed of the tokens. With 10 agents, it is better not to lower the context below 5000.

Enter your question to file question.txt and run agents.py script
