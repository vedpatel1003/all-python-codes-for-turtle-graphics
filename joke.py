# Python joke generator program
import pyjokes

joke = pyjokes.get_joke(language="en", category="all")

print(joke)