# X1 – One extension reserved for fast progress

Assign this only if measured net compulsory coding time is under 90 minutes
and at least 15 minutes remain while preserving the assessment time. Do not
assume fast progress when timing is unknown. Set extra_assigned true once;
there is no second extension.

## A daily summary returned as a structure

In the same project, define a `Summary` type and a function that returns the
count, smallest value and largest value among valid measurements for a requested
date, all in one structure. Include a Boolean member indicating whether any record matched.

The function takes a pointer to readable measurements, an element count and
the requested date. Year, month and day must all match. Initialize minimum
and maximum from the first matching value; do not assume values are positive.
If there is no match, the caller must say so instead of printing meaningless extrema.

Checks with the data after P6:

- 2026-10-17: 5 matches, minimum -2.0, maximum 30.5.
- 2026-10-18: no matches; flag false and count 0.

The fixed assessment follows; do not start another task sequence.
