class Patterns():
    multi_anno = r'(?s)(/\*.*?\*/)'
    single_anno = r'(//.*)'
    require_patt = r'\W(require\(\s*?([\'"]).*?\2\s*?\))'
    import_patt = r'\W(import\s+.*?([\'"]).*?\2)\W'
    export_patt = r'\W(export\s+.*?([\'"]).*?\2)\W'
