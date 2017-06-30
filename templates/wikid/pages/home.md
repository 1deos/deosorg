# home

## Rules

### `A` : Style

* __`00` :__ Use descriptive names for globals, short names for locals.
* __`01` :__ Be consistent.
* __`02` :__ Use active names for functions.
* __`03` :__ Be accurate.
* __`04` :__ Indent to show structure.
* __`05` :__ Use the natural form for expressions.
* __`06` :__ Parenthesize to resolve ambiguity.
* __`07` :__ Break up complex expressions.
* __`08` :__ Be clear.
* __`09` :__ Be careful with side effects.
* __`10` :__ Use a consistent indentation and brace style.
* __`11` :__ Avoid function macros.
* __`12` :__ Parenthesize the macro body and arguments.
* __`13` :__ Give names to magic numbers.
* __`14` :__ Define numbers as constants, not macros.
* __`15` :__ Use character constants, not integers.
* __`16` :__ Use the language to calculate the size of an object.
* __`17` :__ Don't belabor the obvious.
* __`18` :__ Comment functions and global data.
* __`19` :__ Don't comment bad code, rewrite it.
* __`20` :__ Don't contradict the code.
* __`21` :__ Clarify, don't confuse.

---

### `B` : Interfaces

* __`00` :__ Hide implementation details.
* __`01` :__ Choose a small orthogonal set of primitives.
* __`02` :__ Don't reach behind the user's back.
* __`03` :__ Do the same thing the same way everywhere.
* __`04` :__ Free a resource in the same layer that allocated it.
* __`05` :__ Detect errors at a low level, handle them at a high level.
* __`06` :__ Use exceptions only for exceptional situations.

---

### `C` : Debugging

* __`00` :__ Look for familiar patterns.
* __`01` :__ Examine the most recent change.
* __`02` :__ Don't make the same mistake twice.
* __`03` :__ Debug it now, not later.
* __`04` :__ Get a stack trace.
* __`05` :__ Read before typing.
* __`06` :__ Explain your code to someone else.
* __`07` :__ Make the bug reproducible.
* __`08` :__ Divide and conquer.
* __`09` :__ Study the numerology of failures.
* __`10` :__ Display output to localize your search.
* __`11` :__ Write self-checking code.
* __`12` :__ Write a log file.
* __`13` :__ Draw a picture.
* __`14` :__ Use tools.
* __`15` :__ Keep records.

---

### `D` : Testing

* __`00` :__ Test code at its boundaries.
* __`01` :__ Test pre- and post-conditions.
* __`02` :__ Use assertions.
* __`03` :__ Program defensively.
* __`04` :__ Check error returns.
* __`05` :__ Test incrementally.
* __`06` :__ Test simple parts first.
* __`07` :__ Know what output to expect.
* __`08` :__ Verify conservation properties.
* __`09` :__ Compare independent implementations.
* __`10` :__ Measure test coverage.
* __`11` :__ Automate regression testing.
* __`12` :__ Create self contained tests.

---

### `E` : Performance

* __`00` :__ Automate timing measurements.
* __`01` :__ Use a profiler.
* __`02` :__ Concentrate on the hot spots.
* __`03` :__ Draw a picture.
* __`04` :__ Use a better algorithm or data structure.
* __`05` :__ Enable compiler optimizations.
* __`06` :__ Tune the code.
* __`07` :__ Don't optimize what doesn't matter.
* __`08` :__ Collect common subexpressions.
* __`09` :__ Replace expensive operations by cheap ones.
* __`10` :__ Unroll or eliminate loops.
* __`11` :__ Cache frequently-used values.
* __`12` :__ Write a special-purpose allocator.
* __`13` :__ Buffer input and output.
* __`14` :__ Handle special cases separately.
* __`15` :__ Precompute results.
* __`16` :__ Use approximate values.
* __`17` :__ Rewrite in a lower-level language.
* __`18` :__ Save space by using the smallest possible data type.
* __`19` :__ Don't store what you can easily recompute.

---

### `F` : Portability

* __`00` :__ Stick to the standard.
* __`01` :__ Program in the mainstream.
* __`02` :__ Beware of language trouble spots.
* __`03` :__ Try several compilers.
* __`04` :__ Use standard libraries.
* __`05` :__ Use only features available everywhere.
* __`06` :__ Avoid conditional compilation.
* __`07` :__ Localize system dependencies in separate files.
* __`08` :__ Hide system dependencies behind interfaces.
* __`09` :__ Use text for data exchange.
* __`10` :__ Use a fixed byte order for data exchange.
* __`11` :__ Change the name if you change the specification.
* __`12` :__ Maintain compatibility with existing programs and data.
* __`13` :__ Don't assume ASCII.
* __`14` :__ Don't assume English.

---

### `G` : Xanadu

* __`00` :__ Every `Xanadu` server is uniquely and securely identified.
* __`01` :__ Every `Xanadu` server can be operated independently or in a
network.
* __`02` :__ Every user is uniquely and securely identified.
* __`03` :__ Every user can search, retrieve, create and store documents.
* __`04` :__ Every document can consist of any number of parts each of which
may be of any data type.
* __`05` :__ Every document can contain links of any type including virtual
copies ("transclusions") to any other document in the system accessible to its
owner.
* __`06` :__ Links are visible and can be followed from all endpoints.
* __`07` :__ Permission to link to a document is explicitly granted by the act
of publication.
* __`08` :__ Every document can contain a royalty mechanism at any desired
degree of granularity to ensure payment on any portion accessed, including
virtual copies ("transclusions") of all or part of the document.
* __`09` :__ Every document is uniquely and securely identified.
* __`10` :__ Every document can have secure access controls.
* __`11` :__ Every document can be rapidly searched, stored and retrieved
without user knowledge of where it is physically stored.
* __`12` :__ Every document is automatically moved to physical storage
appropriate to its frequency of access from any given location.
* __`13` :__ Every document is automatically stored redundantly to maintain
availability even in case of a disaster.
* __`14` :__ Every `Xanadu` service provider can charge their users at any rate
they choose for the storage, retrieval and publishing of documents.
* __`15` :__ Every transaction is secure and auditable only by the parties to
that transaction.
* __`16` :__ The `Xanadu` client-server communication protocol is an openly
published standard. Third-party software development and integration is
encouraged.

---
