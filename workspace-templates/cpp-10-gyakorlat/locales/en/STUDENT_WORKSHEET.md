# CPP_10 – Quick reference

This is a reference, not another worksheet to fill in. Inno tracks progress.

| Concept | Remember |
|---|---|
| ofstream | Successful default opening truncates existing contents. |
| ios::app | Appends; not used for the complete snapshot here. |
| ifstream >> | Parses numbers and also skips newlines. |
| getline | Isolates a line; does not validate its numbers. |
| istringstream | Parses a string's characters with independent state. |
| ostringstream | Builds text in memory; str() returns a string. |
| eof / fail / bad | EOF / failed operation or bad / serious I/O error; flags can coexist. |
| Boolean conversion | !fail(); not equivalent to is_open(). |
| Header | TICKETS 1 in both languages; version is not count. |
| Temporary object | Replace only after full success; failure preserves the original. |

Headers: iostream – cout, cerr, cin; fstream – file streams; string – string and getline; sstream – string streams. static_cast and return are language constructs. Two int fields require no iomanip/limits or double precision setting.

Venue: 3×4; storage: 4 tickets; first row 4000, other rows 3000. Duplicate row/seat pairs are invalid; another seat in the same row is valid. Only [0,count) is active. Missing header is invalid; a header-only file is a valid empty state.

Inspect actual data after failed operations. Inspect saved files and refresh the view if needed. A new execution starts with empty memory; only loading restores the previous data.
