#! /usr/bin/python
# smart class generator, automatically create getter/setters
# 自动创建getter / settter 方法

# [sample] 
class SmartClass:
    # suppose args = ["name", "age", "gender", "school", "major"]
    def generate(self, args):
        if (args) :
            for ag in args:
                print ag
                
                private_ag = "__%s" % ag
                print private_ag

                # private __name
                if (hasattr(self, private_ag)) :
                    print "[error] already has attribute %s" % private_ag
                else: 
                    setattr(self, private_ag, 0)
            
                # public name
                prop = property()
                
                if (hasattr(self, ag)) :
                    print "[error] already has attribute %s" % private_ag
                else:
                    setattr(self, ag, prop)
        else :
            print "empty args."


sc = SmartClass()
sc.generate(["name", "age", "gender", "school", "major"])
print vars(sc).items()
