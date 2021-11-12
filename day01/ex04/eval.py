class Evaluator:

	def zip_evaluate(words, coefs):
		assert isinstance(words, list) and isinstance(coefs, list), "Error in the values"
		if len(words) != len(coefs):
			return -1
		result = 0
		for i in zip(words, coefs):
			result += len(i[0]) * i[1]
		return result


	def enumerate_evaluate(words, coefs):
		assert isinstance(words, list) and isinstance(coefs, list), "Error in the values"
		if len(words) != len(coefs):
			return -1
		result = 0
		for id,values in enumerate(words):
			result += len(values) * coefs[id];
		return result

words = ["Le", "Lorem", "Ipsum", "est", "simple"]
coefs = [1.0, 2.0, 1.0, 4.0, 0.5]

print (Evaluator.enumerate_evaluate(words, coefs))