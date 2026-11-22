# Test fixtures

Keep these files unchanged. `missing.txt` is deliberately absent. In the table `\n` denotes a newline; empty contents really mean zero bytes.

| File | Exact contents (JSON notation) |
|---|---|
| `even_empty.txt` | `""` |
| `even_newline.txt` | `"3 8\n"` |
| `even_no_newline.txt` | `"2 5 6"` |
| `load_bad.txt` | `"5\nX\n"` |
| `load_blank.txt` | `"\n"` |
| `load_empty.txt` | `""` |
| `load_extra.txt` | `"5 7\n"` |
| `load_full.txt` | `"1\n2\n3\n"` |
| `load_negative.txt` | `"-1\n"` |
| `load_ok.txt` | `"5\n7\n"` |
| `neg_bad.txt` | `"-2 X 4\n"` |
| `neg_empty.txt` | `""` |
| `neg_no_newline.txt` | `"-2"` |
| `neg_ok.txt` | `"-3 0 8 -1\n"` |
