def calculate_frequencies(file_contents):
    # Here is a list of punctuations and uninteresting words you can use to process your text
    punctuations = '''!()-[]{};:'"\,<>./?@#$%^&*_~'''
    uninteresting_words = ["the", "a", "to", "if", "is", "it", "of", "and", "or", "an", "as", "i", "me", "my",
                           "we", "our", "ours", "you", "your", "yours", "he", "she", "him", "his", "her", "hers", "its", "they", "them",
                           "their", "what", "which", "who", "whom", "this", "that", "am", "are", "was", "were", "be", "been", "being",
                           "have", "has", "had", "do", "does", "did", "but", "at", "by", "with", "from", "here", "when", "where", "how",
                           "all", "any", "both", "each", "few", "more", "some", "such", "no", "nor", "too", "very", "can", "will", "just"]

    # LEARNER CODE START HERE
    # created a new list without punctation and formated content as lowercase
    file_content1 = ""
    for char in file_contents:
        if char not in punctuations:
            file_content1 = file_content1 + char
            file_content1 = file_content1.lower()

    # split the new list
    file_content2 = file_content1.split()

    # created a new list without uninteresting words
    file_content3 = ""
    for word in file_content2:
        if word not in uninteresting_words:
            file_content3 = file_content3 + " " + word

    # split the new list
    file_content4 = file_content3.split()

    # dictionary to store keys and values based on frequency count
    # if found in new list increment by one
    # if not find maintain a one count
    file_content = {}
    for content in file_content4:
        if content in file_content.keys():
            file_content[content] += 1
        else:
            file_content[content] = 1

    # wordcloud
    cloud = wordcloud.WordCloud()
    cloud.generate_from_frequencies(file_content)
    return cloud.to_array()
