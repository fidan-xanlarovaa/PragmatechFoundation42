class Question:
    def __init__(self,text,ch,answer):
        self.text=text
        self.ch=ch
        self.answer=answer
    def checkAnswer(self,answer):
        return self.answer==answer


class Quiz:
    def __init__(self,questions):
        self.questions=questions
        self.score=0
        self.questionIndex=0

    def getQuestion(self):
        return self.questions[self.questionIndex]
    
    def displayQuestion(self):
        question = self.getQuestion()
        print(f"Soru {self.questionIndex+1}: {question.text}")

        for i in question.ch:
            print("-"+i)

        answer=input("cevap:  ")
        self.guess=answer
    
    def guess (self,answer):
        question=self.getQuestion()
        if question.checkAnswer(answer):
            self.score +=1
        self.questionIndex +=1

        self.displayQuestion()




q1= Question("en iyi dil hangisi?",["C#","java","python"],"python")
q2= Question("en populer dil hangisi?",["C#","python","java"],"python")
q3= Question("en kazandiran dil hangisi?",["python","C#","java"],"python")
questions=[q1,q2,q3]




