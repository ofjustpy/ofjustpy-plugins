from py_tailwind_utils import *
from pygments.style import Style
from pygments.token import Comment
from pygments.token import Error
from pygments.token import Generic
from pygments.token import Keyword
from pygments.token import Name
from pygments.token import Number
from pygments.token import Operator
from pygments.token import Punctuation
from pygments.token import String
from pygments.token import Text
from pygments.token import Whitespace

# EmacsTailwindStyle = {
#     Whitespace:                "text-gray-400",
#     Comment:                   "italic text-green-700",
#     Comment.Preproc:           "not-italic",
#     Comment.Special:           "not-italic font-bold",

#     Keyword:                   "font-bold text-purple-600",
#     Keyword.Pseudo:            "font-normal",
#     Keyword.Type:              "font-bold text-green-600",

#     Operator:                  "text-gray-600",
#     Operator.Word:             "font-bold text-purple-600",

#     Name.Builtin:              "text-purple-600",
#     Name.Function:             "text-green-500",
#     Name.Class:                "text-blue-700",
#     Name.Namespace:            "font-bold text-blue-700",
#     Name.Exception:            "font-bold text-red-700",
#     Name.Variable:             "text-yellow-600",
#     Name.Constant:             "text-red-800",
#     Name.Label:                "text-yellow-500",
#     Name.Entity:               "font-bold text-gray-500",
#     Name.Attribute:            "text-red-600",
#     Name.Tag:                  "font-bold text-green-700",
#     Name.Decorator:            "text-purple-600",

#     String:                    "text-red-600",
#     String.Doc:                "italic",
#     String.Interpol:           "font-bold text-pink-500",
#     String.Escape:             "font-bold text-orange-600",
#     String.Regex:              "text-pink-500",
#     String.Symbol:             "text-yellow-600",
#     String.Other:              "text-green-700",
#     Number:                    "text-gray-600",

#     Generic.Heading:           "font-bold text-blue-800",
#     Generic.Subheading:        "font-bold text-purple-800",
#     Generic.Deleted:           "text-red-700",
#     Generic.Inserted:          "text-green-500",
#     Generic.Error:             "text-red-500",
#     Generic.Emph:              "italic",
#     Generic.Strong:            "font-bold",
#     Generic.Prompt:            "font-bold text-blue-800",
#     Generic.Output:            "text-gray-300",
#     Generic.Traceback:         "text-blue-300",

#     Error:                     "border-red-500"
# }

EmacsTailwindStyle = {
    Keyword.Constant: [fc / blue / 600, fw.bold],
    Number.Integer: [fc / purple / 700],
    String.Double: [fc / red / 600],
    Punctuation: [fc / gray / 600],
    Text: [fc / gray / 800],
    Whitespace: [fc / gray / 400],
    Comment: [fc / green / 700, fy.i],
    Comment.Preproc: [fy.ni],
    Comment.Special: [fy.ni, fw.bold],
    Comment.Single: [fc/gray/600, fw.thin],
    
    Keyword: [fw.bold, fc / purple / 600],
    Keyword.Pseudo: [fw.normal],
    Keyword.Type: [fw.bold, fc / green / 600],
    Keyword.Namespace: [fw.bold, fc/blue/700],
    Operator: [fc / gray / 600],
    Operator.Word: [fw.bold, fc / purple / 600],
    Name: [fc / green / 700],
    Name.Builtin: [fc / purple / 600],
    Name.Function: [fc / green / 500],
    Name.Class: [fc / blue / 700],
    Name.Namespace: [fw.bold, fc / blue / 700],
    Name.Exception: [fw.bold, fc / red / 700],
    Name.Variable: [fc / yellow / 600],
    Name.Constant: [fc / red / 800],
    Name.Label: [fc / yellow / 500],
    Name.Entity: [fw.bold, fc / gray / 500],
    Name.Attribute: [fc / red / 600],
    Name.Tag: [fw.bold, fc / green / 700],
    Name.Decorator: [fc / purple / 600],
    String: [fc / red / 600],
    String.Doc: [fy.i],
    String.Interpol: [fw.bold, fc / pink / 500],
    String.Escape: [fw.bold, fc / orange / 600],
    String.Regex: [fc / pink / 500],
    String.Symbol: [fc / yellow / 600],
    String.Other: [fc / green / 700],
    Number: [fc / gray / 600],
    Generic.Heading: [fw.bold, fc / blue / 800],
    Generic.Subheading: [fw.bold, fc / purple / 800],
    Generic.Deleted: [fc / red / 700],
    Generic.Inserted: [fc / green / 500],
    Generic.Error: [fc / red / 500],
    Generic.Emph: [fy.i],
    Generic.Strong: [fw.bold],
    Generic.Prompt: [fw.bold, fc / blue / 800],
    Generic.Output: [fc / gray / 300],
    Generic.Traceback: [fc / blue / 300],
    Error: [bd / red / 500],
}
