# -*- coding: utf-8 -*-
import base64
import marshal
import zlib

input_file = 'Raja-VauTeach-world.py'
output_file = 'Raja-VauTeach-protected.py'

try:
    with open(input_file, 'r', encoding='utf-8') as f:
        source_code = f.read()

    # Compile, compress and encode
    code_obj = compile(source_code, '<string>', 'exec')
    marshalled = marshal.dumps(code_obj)
    compressed = zlib.compress(marshalled)
    encoded = base64.b64encode(compressed)

    # Protected wrapper runner
    protected_code = (
        '# -*- coding: utf-8 -*-\n'
        'import base64, marshal, zlib\n'
        f"exec(marshal.loads(zlib.decompress(base64.b64decode({repr(encoded)}))))\n"
    )

    with open(output_file, 'w', encoding='utf-8') as f:
        f.write(protected_code)

    print(f'\n[✓] SUCCESS! Protected file saved as: {output_file}')
except Exception as e:
    print(f'\n[!] Error: {e}')
