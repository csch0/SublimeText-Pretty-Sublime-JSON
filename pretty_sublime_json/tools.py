import sublime

import json
import re


def decode_value(string):
    try:
        if hasattr(sublime, 'decode_value'):
            value = sublime.decode_value(string)
        else:
            string = re.sub(re.compile(r"//.*?\n"), "", string)
            string = re.sub(re.compile(r"/\*.*?\*/", re.DOTALL), "", string)
            value = json.loads(string)
    except:
        value = None

    return value if value else []


def encode_value(value, sort_by, pretty=True):
    lstItems = []
    for objItem in sorted(value, key=lambda x: [x[key] for key in sort_by]):
        lstFields = []
        if "keys" in objItem:
            lstFields += ["\"keys\": " + json.dumps(objItem["keys"], ensure_ascii=False)]
        if "caption" in objItem:
            lstFields += ["\"caption\": " + json.dumps(objItem["caption"], ensure_ascii=False)]
        if "command" in objItem:
            lstFields += ["\"command\": " + json.dumps(objItem["command"], ensure_ascii=False) + (", \"args\": " + json.dumps(objItem["args"], ensure_ascii=False, sort_keys=True) if "args" in objItem else "")]
        if "context" in objItem:
            lstFields += ["\"context\": [" + ",".join(["\n\t\t\t" + json.dumps(item, ensure_ascii=False, sort_keys=True) for item in sorted(objItem["context"], key=lambda x: x["key"])]) + "\n\t\t]"]
        lstItems += ["\n\t{\n\t\t" + ",\n\t\t".join(lstFields) + "\n\t}"]
    value = "[" + ",".join(lstItems) + "\n]"
    return value
