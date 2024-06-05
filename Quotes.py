import random


class Quotes:
    def __init__(self):
        self.quotes = [
            "Don't worry about what anybody else is going to do. The best way to predict the future is to invent it. -- Alan Kay",
            "Premature optimization is the root of all evil (or at least most of it) in programming. -- Donald Knuth",
            "Lisp has jokingly been called 'the most intelligent way to misuse a computer'. I think that description is a great compliment because it transmits the full flavor of liberation: it has assisted a number of our most gifted fellow humans in thinking previously impossible thoughts. -- Edsger Dijkstra, CACM, 15:10",
            "Keep away from people who try to belittle your ambitions. Small people always do that, but the really great make you feel that you, too, can become great. -- Mark Twain",
            "The problem is that small examples fail to convince, and large examples are too big to follow. -- Steve Yegge.",
            "We are the sum of our behaviours; excellence therefore is not an act but a habit. -- Aristotle.",
            "The purpose of abstraction is not to be vague, but to create a new semantic level in which one can be absolutely precise. -- Edsger Dijkstra",
            "Every man prefers belief to the exercise of judgment. -- Seneca",
            "It’s hard to grasp abstractions if you don’t understand what they’re abstracting away from. -- Nathan Weizenbaum",
            "That is one of the most distinctive differences between school and the real world: there is no reward for putting in a good effort. In fact, the whole concept of a 'good effort' is a fake idea adults invented to encourage kids. It is not found in nature. -- Paul Graham",
            "I find that the harder I work, the more luck I seem to have. -- Thomas Jefferson",
            "Don't stay in bed, unless you can make money in bed. -- George Burns",
            "If everything seems under control, you're not going fast enough. -- Mario Andretti",
            "Chance favors the prepared mind. -- Louis Pasteur",
            "Controlling complexity is the essence of computer programming. -- Brian Kernigan",
            "The function of good software is to make the complex appear to be simple. -- Grady Booch",
            "Programmers are in a race with the Universe to create bigger and better idiot-proof programs, while the Universe is trying to create bigger and better idiots. So far the Universe is winning. -- Rich Cook",
            "A hacker on a roll may be able to produce–in a period of a few months–something that a small development group (say, 7-8 people) would have a hard time getting together over a year. IBM used to report that certain programmers might be as much as 100 times as productive as other workers, or more. -- Peter Seebach",
            "The best programmers are not marginally better than merely good ones. They are an order-of-magnitude better, measured by whatever standard: conceptual creativity, speed, ingenuity of design, or problem-solving ability. -- Randall E. Stross",
            "A great lathe operator commands several times the wage of an average lathe operator, but a great writer of software code is worth 10,000 times the price of an average software writer. -- Bill Gates",
            "Measuring programming progress by lines of code is like measuring aircraft building progress by weight. -- Bill Gates",
            "First learn computer science and all the theory. Next develop a programming style. Then forget all that and just hack. -- George Carrette",
            "To iterate is human, to recurse divine. -- L. Peter Deutsch",
            "The best thing about a boolean is even if you are wrong, you are only off by a bit. -- Anonymous",
            "Should array indices start at 0 or 1? My compromise of 0.5 was rejected without, I thought, proper consideration. -- Stan Kelly-Bootle",
            "The use of COBOL cripples the mind; its teaching should therefore be regarded as a criminal offense. -- E.W. Dijkstra",
            "It is practically impossible to teach good programming style to students that have had prior exposure to BASIC. As potential programmers, they are mentally mutilated beyond hope of regeneration. -- E. W. Dijkstra",
            "One of the main causes of the fall of the Roman Empire was that–lacking zero–they had no way to indicate successful termination of their C programs. -- Robert Firth",
            "Saying that Java is nice because it works on all OSes is like saying that anal sex is nice because it works on all genders. -- Alanna",
            "If Java had true garbage collection, most programs would delete themselves upon execution. -- Robert Sewell",
            "Software is like sex: It’s better when it’s free. -- Linus Torvalds",
            "Any code of your own that you haven’t looked at for six or more months might as well have been written by someone else. -- Eagleson’s Law",
            "Good programmers use their brains, but good guidelines save us having to think out every case. -- Francis Glassborow",
            "Considering the current sad state of our computer programs, software development is clearly still a black art, and cannot yet be called an engineering discipline. -- Bill Clinton",
            "If debugging is the process of removing bugs, then programming must be the process of putting them in. -- Edsger W. Dijkstra",
            "Always code as if the guy who ends up maintaining your code will be a violent psychopath who knows where you live. -- Martin Golding",
            "Everything that can be invented has been invented. -- Charles H. Duell, Commissioner, U.S. Office of Patents, 1899",
            "I think there’s a world market for about 5 computers. -- Thomas J. Watson, Chairman of the Board, IBM, circa 1948",
            "It would appear that we have reached the limits of what it is possible to achieve with computer technology, although one should be careful with such statements, as they tend to sound pretty silly in 5 years. -- John Von Neumann, circa 1949",
            "But what is it good for? -- Engineer at the Advanced Computing Systems Division of IBM, commenting on the microchip, 1968",
            "There is no reason for any individual to have a computer in his home. -- Ken Olson, President, Digital Equipment Corporation, 1977",
            "640K ought to be enough for anybody. -- Bill Gates, 1981",
            "Windows NT addresses 2 Gigabytes of RAM, which is more than any application will ever need. -- Microsoft, on the development of Windows NT, 1992",
            "We will never become a truly paper-less society until the Palm Pilot folks come out with WipeMe 1.0. -- Andy Pierson",
            "If it keeps up, man will atrophy all his limbs but the push-button finger. -- Frank Lloyd Wright",
            "Functional programming is like describing your problem to a mathematician. Imperative programming is like giving instructions to an idiot. -- arcus, #scheme on Freenode",
            "Its a shame that the students of our generation grew up with windows and mice because that tainted our mindset not to think in terms of powerful tools. Some of us are just so tainted that we will never recover. -- Jeffrey Mark Siskind <qobi@research.nj.nec.com> in comp.lang.lisp",
            "Lisp is a programmable programming language. -- John Foderaro to the quotes list"
        ]
        self.shuffled_quotes = self.quotes.copy()

    def get_random_quote(self):
        if not self.shuffled_quotes:
            self.shuffled_quotes = self.quotes.copy()
            random.shuffle(self.shuffled_quotes)
        quote = self.shuffled_quotes.pop()
        return quote

    def get_recursive_quote(self):
        if not self.quotes:
            return None
        quote = self.get_random_quote()
        self.quotes.remove(quote)
        next_quote = self.get_recursive_quote()
        if next_quote is not None:
            self.quotes.append(quote)
        return quote


quotes = Quotes()
