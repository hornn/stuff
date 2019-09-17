import sys
import textwrap
from collections import namedtuple

TRUES = ['true', 't', 'yes', 'y']
FALSES = ['false', 'f', 'no', 'n']

QuestionAndScore = namedtuple('QuestionAndScore', 'question score')
QuestionsAndTitles = namedtuple('QuestionsAndTitles', 'questions low_desc high_desc')

QUESTIONS_AND_SCORES = {
    'Resilience': QuestionsAndTitles([
        #[1, 3, 5, 6, 8, 10]
        QuestionAndScore(
            "If I have a minor disagreement with a close friend of spouse - closer to \"No, it's your turn to do"
            "the dishes\" than \"You cheapted on me?!\" - it typically leaves me out of sorts for hours or longer.",
            True
        ),
        QuestionAndScore(
            "If another driver uses the shoulder to zoom up to the front of a long line of traffic waiting to merge, "
            "I am likely to shake it off easily rather than fume about it for a long time.",
            False
        ),
        QuestionAndScore(
            "When I have experienced profound grief, such as the death of someone close to me, "
            "it has interfered with my ability to function for many months.",
            True
        ),
        QuestionAndScore(
            "If I make a mistake at work and get reprimanded for it, I can shrug it off and take it as a learning "
            "experience.",
            False
        ),
        QuestionAndScore(
            "If I try a new restaurant and find that the food is awful and the service snooty, it ruins my whole evening.",
            True
        ),
        QuestionAndScore(
            "If I'm stuck in traffic because of an accident up ahead, when I pass the bottleneck I typically floor it to "
            "vent my frustration but still seethe inside.",
            True
        ),
        QuestionAndScore(
            "If my home's water heater breaks, it does not affect my mood very much, since I know I can just call a "
            "plumber and get it fixed.",
            False
        ),
        QuestionAndScore(
            "If I meet a wonderful man/woman and ask if he/she would like to get together again, being told no typically "
            "puts me in a bad mood for hours or even days.",
            True
        ),
        QuestionAndScore(
            "If I am being considered for an important professional award or promotion and it goes to someone I consider "
            "less qualified, I can usually move on quickly.",
            False
        ),
        QuestionAndScore(
            "At a party, if I'm having a conversation with an interesting stranger and get completely tongue-tied when "
            "he/she asks me about myself, I tend to replay the conversion - this time including what I should have said - "
            "for hours or even days afterward.",
            True
        )
    ], 'Fast to Recover', 'Slow to Recover'),
    'Outlook': QuestionsAndTitles([
        # [1, 3, 6, 8, 10]
        QuestionAndScore(
            "When I am invited to meet new people, I look forward to it, thinking they might become my friends, "
            "rather than seeing it as a chore, figuring these people will never be worth knowing.",
            True
        ),
        QuestionAndScore(
            "When evaluating a coworker, I focus on details about which areas he needs to improve rather than on his "
            "positive overall performance.",
            False
        ),
        QuestionAndScore(
            "I believe the next ten years will be better for me than the last ten.",
            True
        ),
        QuestionAndScore(
            "Faced with the possibility of moving to a new city, I regard it as a frightening step into the unknown.",
            False
        ),
        QuestionAndScore(
            "When something small but unexpected and positive happens to me in the morning - for example, having a "
            "great conversation with a stranger - the positive mood fades within minutes.",
            False
        ),
        QuestionAndScore(
            "When I go to a party and I'm having a good time at the outset, the positive feeling tends to last for the "
            "entire evening.",
            True
        ),
        QuestionAndScore(
            "I find that beautiful scenes such as a gorgeous sunset quickly wear off and I get bored easily.",
            False
        ),
        QuestionAndScore(
            "When I wake up in the morning I can think of a pleasant activity that I've planned, and the thought "
            "puts me in a good mood that lasts the entire day.",
            True
        ),
        QuestionAndScore(
            "When I go to a museum or attend a concert, the first few minutes are really enjoyable, but it doesn't "
            "last.",
            False
        ),
        QuestionAndScore(
            "I often feel that on busy days I can keep going from one event to the next without getting tired",
            True
        )
    ], 'Negative', 'Positive'),
    'Social Intuition': QuestionsAndTitles([
        # [1, 2, 4, 7, 8, 10]
        QuestionAndScore(
            "When I'm talking with people, I often notice subtle social cues about their emotions - discomfort, say, "
            "or anger - before they acknowledge those feelings in themselves.",
            True
        ),
        QuestionAndScore(
            "I often find myself noting facial expressions and body language.",
            True
        ),
        QuestionAndScore(
            "I find it does not really matter if I talk with people on the phone or in person, since I rarely get any "
            "additional information from seeing whom I'm speaking with.",
            False
        ),
        QuestionAndScore(
            "I often feel as though I know more about people's true feelings than they do themselves.",
            True
        ),
        QuestionAndScore(
            "I am often taken by surprise when someone I'm talking with gets angry or upset at something I said, for "
            "no apparent reason.",
            False
        ),
        QuestionAndScore(
            "At a restaurant, I prefer to sit next to someone I'm speaking with so I don't have to see his or her full "
            "face.",
            False
        ),
        QuestionAndScore(
            "I often find myself responding to another person's discomfort or distress on the basis of an intuitive "
            "feel rather than an explicit discussion.",
            True
        ),
        QuestionAndScore(
            "When I am in public places with time to kill, I like to observe people around me.",
            True
        ),
        QuestionAndScore(
            "I find it uncomfortable when someone I barely know looks directly into my eyes during a conversation.",
            False
        ),
        QuestionAndScore(
            "I can often tell when something is bothering another person just by looking at him or her.",
            True
        )
    ], 'Puzzled', 'Socially Intuitive'),
    'Self-Awareness': QuestionsAndTitles([
        # [4, 5, 7, 8, 10]
        QuestionAndScore(
            "Often, when someone asks me why I am so angry or sad, I response (or think to myself), \"But I'm not!\"",
            False
        ),
        QuestionAndScore(
            "When those closest to me ask why I treated someone brusquely or meanly, I often disagree that I did any "
            "such thing.",
            False
        ),
        QuestionAndScore(
            "I frequently - more than a couple of times a month - find that my heart is racing or my pulse is "
            "pounding, and I have no idea why.",
            False
        ),
        QuestionAndScore(
            "When I observe someone in pain, I feel the pain myself both emotionally and physically.",
            True
        ),
        QuestionAndScore(
            "I am usually sure enough about how I am feeling that I can put my emotions into words.",
            True
        ),
        QuestionAndScore(
            "I sometimes notice aches and pains and have no idea where they came from.",
            False
        ),
        QuestionAndScore(
            "I like to spend time being quiet and relaxed, just feeling what is going on inside me.",
            True
        ),
        QuestionAndScore(
            "I believe I very much inhabit my body and feel at home and comfortable with my body.",
            True
        ),
        QuestionAndScore(
            "I am strongly oriented to the external world and rarely take note of what's happening in my body.",
            False
        ),
        QuestionAndScore(
            "When I exercise, I am very sensitive to the changes it produces in my body.",
            True
        ),
    ], 'Self-Opaque', 'Self-Aware'),
    'Sensitivity to Context': QuestionsAndTitles([
        # [ 1, 5, 6, 8, 9, 10]
        QuestionAndScore(
            "I have been told by someone close to me that I am unusually sensitive to other people's feelings.",
            True
        ),
        QuestionAndScore(
            "I have occasionally been told that I behaved in a socially inappropriate way, which surprised me.",
            False
        ),
        QuestionAndScore(
            "I have sometimes suffered a setback at work or had a falling-out with a friend because I was too "
            "chummy with a superior or too jovial when a good friend was distraught.",
            False
        ),
        QuestionAndScore(
            "When I speak with people, they sometimes move back ot increase the distance between us.",
            False
        ),
        QuestionAndScore(
            "I often find myself censoring what I was about to say because I've sensed something in the situation "
            "that would make it inappropriate (e.g., before I respond to, \"Honey, do these jeans make me look fat?\").",
            True
        ),
        QuestionAndScore(
            "When I am in a public setting like a restaurant, I am especially aware of modulating how loudly I speak.",
            True
        ),
        QuestionAndScore(
            "I have frequently been reminded when in public to avoid mentioning the names of people who might be "
            "around.",
            False
        ),
        QuestionAndScore(
            "I am almost always aware of whether I have been someplace before, even if it is a highway that I last "
            "drove many years ago.",
            True
        ),
        QuestionAndScore(
            "I notice when someone is acting in a way that seems out of place, such as behaving too casually at work.",
            True
        ),
        QuestionAndScore(
            "I've been told by those close to me tah I show good manners with strangers and in new situations.",
            True
        ),
    ], 'Tuned-Out', 'Tuned-In'),
    'Attention': QuestionsAndTitles([
        # [1, 2, 3, 6, 7, 10]
        QuestionAndScore(
            "I can concentrate in a noisy environment.",
            True
        ),
        QuestionAndScore(
            "When I am in a situation in which a lot is going on and there is a great deal of sensory stimulation, "
            "such as at a party or in a crowd at an airport, I can keep myself from getting lost in a train of thought "
            "about any particular thing I see.",
            True
        ),
        QuestionAndScore(
            "If I decide to focus my attention on a particular task, I find that I am mostly able to keep it there.",
            True
        ),
        QuestionAndScore(
            "If I am at home and trying to work, the noises of a television or other people make me very distracted.",
            False
        ),
        QuestionAndScore(
            "I find that if I sit quietly for even a few moments, a flood of thoughts rush into my mind and I find "
            "myself following multiple strands of thought, often without knowing how each one began.",
            False
        ),
        QuestionAndScore(
            "If I am distracted by some unexpected event, I can refocus my attention on what I had been doing.",
            True
        ),
        QuestionAndScore(
            "During periods of relative quiet, such as when I'm sitting on a train or a bus or waiting in line at a "
            "store, I notice a lot of the things around me.",
            True
        ),
        QuestionAndScore(
            "When an important solo project requires my full and focused attention, I try to work in the quietest "
            "place I can find.",
            False
        ),
        QuestionAndScore(
            "My attention tends to get captured by stimuli and events in the environment, and it is difficult for me "
            "to disengage once this happens.",
            False
        ),
        QuestionAndScore(
            "It is easy for me to talk with another person in a crowded situation like a cocktail party or a cubicle "
            "in an office; I can tune out others in such an environment even when, with concentration, I can make "
            "out what they are saying.",
            True
        ),
    ], 'Unfocused', 'Focused')
}


def question(msg):
    wrapper = textwrap.TextWrapper(width=70)
    word_list = wrapper.wrap(text=msg)
    print '*' * 70
    for element in word_list:
        print element
    answer = None
    while answer is None:
        print "Answer True/False:"
        read = sys.stdin.readline().strip().lower()
        if read in TRUES:
            answer = True
        elif read in FALSES:
            answer = False
    return answer


def calculate_score(result, expected):
    if result is expected:
        return 1
    return 0


def calculate_scores(results, index):
    score = 0
    for res, expected in zip(results, index):
        if res is expected:
            score += 1
    return score


def print_score(score, title, low_desc, high_desc):
    print "Your %s score is %d / 10" % (title, score)
    pretty_score = '%s> %d <%s' % ('-' * (6*(score-1)), score, '-' * 6*(10-score))
    print pretty_score
    print "1 %s 10" % ('-' * 55)
    print "%s%s" % (low_desc.ljust(30, ' '), high_desc.rjust(30, ' '))


def run_test():
    print "Please enter the name of the person about whom you answer:\n"
    name = sys.stdin.readline().strip()
    print "Thank you"

    print "Answer True or False for each question. Do not hesitate or think long."

    results = {}
    for category, qandt in QUESTIONS_AND_SCORES.iteritems():
        print '*' * 70
        print ('Testing %s' % category).center(70, ' ')
        print '*' * 70

        total = 0
        questions = qandt.questions
        for item in questions:
            res = question(item.question)
            total += calculate_score(res, item.score)
        results[category] = total

    print '*' * 70
    print "The results for %s are:" % name
    for (category, total) in results.iteritems():
        print '*' * 70
        titles = QUESTIONS_AND_SCORES[category]
        print_score(total, category, titles.low_desc, titles.high_desc)


if __name__ == '__main__':
    run_test()
