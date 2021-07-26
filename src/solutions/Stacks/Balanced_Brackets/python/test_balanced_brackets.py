import unittest
from unittest import result
from solution import isBalanced

TestResults = [
    {
        "Expected": True
    },
    {
        "Expected": False
    },
    {
        "Expected": False
    },
    {
        "Expected": False
    },
    {
        "Expected": True
    },
    {
        "Expected": True
    },
    {
        "Expected": True
    },
    {
        "Expected": True
    },
    {
        "Expected": True
    },
    {
        "Expected": True
    },
    {
        "Expected": True
    },
    {
        "Expected": False
    },
    {
        "Expected": False
    },
    {
        "Expected": False
    },
    {
        "Expected": True
    },
    {
        "Expected": False
    },
    {
        "Expected": True
    },
    {
        "Expected": False
    },
    {
        "Expected": False
    },
    {
        "Expected": False
    },
    {
        "Expected": True
    },
    {
        "Expected": True
    },
    {
        "Expected": True
    }
]
JSONTests = [
    {
        "string": "([])(){}(())()()"
    },
    {
        "string": "()[]{}{"
    },
    {
        "string": "(((((({{{{{[[[[[([)])]]]]]}}}}}))))))"
    },
    {
        "string": "()()[{()})]"
    },
    {
        "string": "(()())((()()()))"
    },
    {
        "string": "{}()"
    },
    {
        "string": "()([])"
    },
    {
        "string": "((){{{{[]}}}})"
    },
    {
        "string": "((({})()))"
    },
    {
        "string": "(([]()()){})"
    },
    {
        "string": "(((((([[[[[[{{{{{{{{{{{{()}}}}}}}}}}}}]]]]]]))))))((([])({})[])[])[]([]){}(())"
    },
    {
        "string": "{[[[[({(}))]]]]}"
    },
    {
        "string": "[((([])([]){}){}){}([])[]((())"
    },
    {
        "string": ")[]}"
    },
    {
        "string": "(a)"
    },
    {
        "string": "(a("
    },
    {
        "string": "(141[])(){waga}((51afaw))()hh()"
    },
    {
        "string": "aafwgaga()[]a{}{gggg"
    },
    {
        "string": "(((((({{{{{safaf[[[[[([)]safsafsa)]]]]]}}}gawga}}))))))"
    },
    {
        "string": "()(agawg)[{()gawggaw})]"
    },
    {
        "string": "(()agwg())((()agwga()())gawgwgag)"
    },
    {
        "string": "{}gawgw()"
    },
    {
        "string": "(agwgg)([ghhheah%\u0026@Q])"
    }
]


class BalancedBracketsTest(unittest.TestCase):
    def test_is_balanced(self):
        for i in range(0, len(JSONTests)):
            str = JSONTests[i]['string']
            result = isBalanced(str)
            self.assertEqual(result, TestResults[i]['Expected'])
