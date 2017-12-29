from kivy.app import App
#kivy.require("1.8.0")
from kivy.uix.floatlayout import FloatLayout
from kivy.uix.widget import Widget
from kivy.lang import Builder

 

Builder.load_string("""
<Button>:
	size_hint: 0.1,0.1

        
<LineBezier>:
    canvas:
        Color:
            rgba: .1, .1, 1, .9
        Line:
            width: 2.
            points:(self.x+500, self.y-50,self.x+500, self.y+1000),
            
            
                
<FloatLayout>:
    canvas:
        Color:
            rgba: 1,1,1,1
        Rectangle:
            size: 150,250
            pos: 580,180
               
 
    LineBezier:
        
    Label:
        text: 'Items in Fridge'
        pos: -150,250 
        font_size:26
    
    Label:
        text: 'Sno.'
        pos: -320,170
    Label:
        text: 'Name'
        pos: -150,170
    Label:
        text: 'Quantity'
        pos: 20,170     
    Label:
        text: 'Place the Bar-Code in the area below'
        pos: 260,170         
                    
    Button:
               	    
		pos_hint: {'left': 1, 'top': 1}
		background_normal: 'icon-left.png'
		    
	
	Button:
   
		pos_hint: {'right': 1, 'top': 1}
		background_normal: 'icon-right.png'
		
		
	
""")

class LineBezier(Widget):
    pass

class Rectangle(Widget):
    pass

class KhaakSimpleKivy(App):
    def build(self):
        FloatLayout().add_widget(LineBezier())
        FloatLayout().add_widget(Rectangle())
        return FloatLayout()

if __name__ == "__main__":
    KhaakSimpleKivy().run()

