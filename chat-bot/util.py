qna = {
	"what is ai community?": "It aims to advance AI, promote ethical development, and facilitate knowledge sharing. The community covers topics like machine learning, neutral networks, and computer vision.",
	"what are the objectives and aspirations of the ai community?": "To advance AI technology, promote ethical practices, and encourage collaboration and knowledge sharing. The community aims to create a network of practitioners and researchers who work together to innovate while considering the thical implications and broader impact of AI.",
	"what kind of topics and materials are typically covered in ai community sessions": "AI community sessions include machine learning, neural network, natural language processing , computer vision, AI thics, AI applications, cutting-edge research, and practical implementation.",
	"when are the community sessions held?": "AI community sessions are held on every Wednesday at 3:00 PM.",
	"what are the ai fields?": "They are machine learning, computer vision, deep learning, NLP, robotics.",
	"what are tools and languages used in ai?": "Python, TensorFlow, PyTorch, scikit-learn, Keras, Juptyr, matlab, R, Docker",
	"is ai used in cybersecurity?": "AI is used to detect and mitigate threats, identify anomalies, and enhance defense mechanisms.",
	"what are the ethical consideration in ai?": "This topic explores the thical implication of AI, such as fairness, accountabiity, transparency, and privacy.",
}

def get_response(question):
	return qna[question] if question in qna else "I am not capable of answering your question."