class PromptModifier(object):

    def __init__(self, append):
        self.append = append

    def applyChanges(self, prompt):
        mPrompt = prompt + self.append
        return mPrompt