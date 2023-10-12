from langchain.prompts import PromptTemplate
from langchain.chat_models import ChatOpenAI
from langchain.chains import LLMChain

information= """
    Emily Elizabeth Dickinson (December 10, 1830 – May 15, 1886) was an American poet. Little-known during her life, she has since been regarded as one of the most important figures in American poetry.[2] Dickinson was born in Amherst, Massachusetts, into a prominent family with strong ties to its community. After studying at the Amherst Academy for seven years in her youth, she briefly attended the Mount Holyoke Female Seminary before returning to her family's home in Amherst. Evidence suggests that Dickinson lived much of her life in isolation. Considered an eccentric by locals, she developed a penchant for white clothing and was known for her reluctance to greet guests or, later in life, even to leave her bedroom. Dickinson never married, and most of her friendships were based entirely upon correspondence.[3]

    While Dickinson was a prolific writer, her only publications during her lifetime were 10 of her nearly 1,800 poems, and one letter.[4] The poems published then were usually edited significantly to fit conventional poetic rules. Her poems were unique for her era; they contain short lines, typically lack titles, and often use slant rhyme as well as unconventional capitalization and punctuation.[5] Many of her poems deal with themes of death and immortality, two recurring topics in letters to her friends, and also explore aesthetics, society, nature, and spirituality.[6]

    Although Dickinson's acquaintances were most likely aware of her writing, it was not until after her death in 1886—when Lavinia, Dickinson's younger sister, discovered her cache of poems—that her work became public. Her first collection of poetry was published in 1890 by personal acquaintances Thomas Wentworth Higginson and Mabel Loomis Todd, though both heavily edited the content. A complete collection of her poetry became available for the first time when scholar Thomas H. Johnson published The Poems of Emily Dickinson in 1955.[7] In 1998, The New York Times reported on an infrared technology study revealing that much of Dickinson's work had been deliberately censored to exclude the name "Susan".[8] At least eleven of Dickinson's poems were dedicated to her sister-in-law Susan Huntington Gilbert Dickinson, though all the dedications were obliterated, presumably by Todd.[8] These edits work to censor the nature of Emily and Susan's relationship, which many scholars have interpreted as romantic.[9][10][11]
"""

if __name__== '__main__':
    print("Hello LangChain")

    summary_template = """
        Given the information {information} about a person from I want you to create:
        1. a short summary
        2. two interesting facts about them
    """

    summary_prompt_template = PromptTemplate(
        input_variables=["information"], template=summary_template
    )

    llm = ChatOpenAI(temperature=0, model_name='gpt-3.5-turbo')

    chain = LLMChain(llm=llm, prompt=summary_prompt_template)

    print(chain.run(information=information))
    print('end')