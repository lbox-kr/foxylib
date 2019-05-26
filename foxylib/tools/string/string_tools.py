import ast


def str2strip(s): return s.strip() if s else s
def str2rstrip(s): return s.rstrip() if s else s
def str2splitlines(s): return s.splitlines() if s else s
def str2lower(s): return s.lower() if s else s
def format_str(s, *args, **kwargs): return s.format(*args, **kwargs) if s else s
def join_str(s, *args, **kwargs): return s.join(*args, **kwargs) if s else s




class StringToolkit:
    @classmethod
    def quoted2stripped(cls, s_IN, ):
        try:
            module = ast.parse(s_IN)
        except SyntaxError:
            return s_IN

        node_list = module.body
        if len(node_list) != 1: return s_IN

        node_Expr = node_list[0]
        if not isinstance(node_Expr, ast.Expr): return s_IN

        node_Str = node_Expr.value
        if not isinstance(node_Str, ast.Str): return s_IN

        return node_Str.s

    @classmethod
    def str_se2str(cls, s, se):
        if se is None: return None

        return s[se[0]:se[1]]

    @classmethod
    def str2split(cls, s, *args,**kwargs): return s.split(*args,**kwargs) if s else s

    @classmethod
    def escape_quotes(cls, s):
        return s.replace('"', '\\"').replace("'", "\\'")

    @classmethod
    def escape_doublequotes(cls, s):
        return s.replace('"', '\\"')

    @classmethod
    def query2indices(cls, s_query, s_doc):
        start = 0
        while True:

            i = s_doc.find(s_query, start)
            if i < 0: break

            yield i
            start = i+1

    @classmethod
    def span2strip(cls, ipair, str_in):
        if not ipair:
            return ipair

        s, e = ipair

        s_match = str_in[s:e]
        s_strip = s_match.strip()

        i_start = s_match.find(s_strip)

        s_out = s + i_start
        e_out = s_out + len(s_strip)

        return (s_out, e_out)

str2split = StringToolkit.str2split
escape_quotes = StringToolkit.escape_quotes
escape_doublequotes = StringToolkit.escape_doublequotes
