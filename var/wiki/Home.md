# ΔOS: Decentralized Operating System

> *The languages of intelligence (writing) and self-interest (money) are the*
> *mind's greatest creations; both must be decentralized or all is lost.*
> **[—DeSantis](https://twitter.com/desantis/status/795023340704595968)**

<table>
  <tbody>
    <tr>
    </tr>
    <tr>
      <td>
        <h5>Contents</h5>
        <b>﹂</b> <a href="#rules">
        Rules
        </a><br>
        <b>&nbsp;&nbsp;&nbsp;﹂</b> <a href="#style">
        Style
        </a><br>
        <b>&nbsp;&nbsp;&nbsp;﹂</b> <a href="#interfaces">
        Interfaces
        </a><br>
        <b>&nbsp;&nbsp;&nbsp;﹂</b> <a href="#debugging">
        Debugging
        </a><br>
        <b>&nbsp;&nbsp;&nbsp;﹂</b> <a href="#testing">
        Testing
        </a><br>
        <b>&nbsp;&nbsp;&nbsp;﹂</b> <a href="#performance">
        Performance
        </a><br>
        <b>&nbsp;&nbsp;&nbsp;﹂</b> <a href="#portability">
        Portability
        </a><br>
        <b>&nbsp;&nbsp;&nbsp;﹂</b> <a href="#xanadu">
        Xanadu
        </a><br>
      </td>
    </tr>
  </tbody>
</table>

## Rules

### Style

* Use descriptive names for globals, short names for locals.
* Be consistent.
* Use active names for functions.
* Be accurate.
* Indent to show structure.
* Use the natural form for expressions.
* Parenthesize to resolve ambiguity.
* Break up complex expressions.
* Be clear.
* Be careful with side effects.
* Use a consistent indentation and brace style.
* Avoid function macros.
* Parenthesize the macro body and arguments.
* Give names to magic numbers.
* Define numbers as constants, not macros.
* Use character constants, not integers.
* Use the language to calculate the size of an object.
* Don't belabor the obvious.
* Comment functions and global data.
* Don't comment bad code, rewrite it.
* Don't contradict the code.
* Clarify, don't confuse.

### Interfaces

* Hide implementation details.
* Choose a small orthogonal set of primitives.
* Don't reach behind the user's back.
* Do the same thing the same way everywhere.
* Free a resource in the same layer that allocated it.
* Detect errors at a low level, handle them at a high level.
* Use exceptions only for exceptional situations.

### Debugging

* Look for familiar patterns.
* Examine the most recent change.
* Don't make the same mistake twice.
* Debug it now, not later.
* Get a stack trace.
* Read before typing.
* Explain your code to someone else.
* Make the bug reproducible.
* Divide and conquer.
* Study the numerology of failures.
* Display output to localize your search.
* Write self-checking code.
* Write a log file.
* Draw a picture.
* Use tools.
* Keep records.

### Testing

* Test code at its boundaries.
* Test pre- and post-conditions.
* Use assertions.
* Program defensively.
* Check error returns.
* Test incrementally.
* Test simple parts first.
* Know what output to expect.
* Verify conservation properties.
* Compare independent implementations.
* Measure test coverage.
* Automate regression testing.
* Create self contained tests.

### Performance

* Automate timing measurements.
* Use a profiler.
* Concentrate on the hot spots.
* Draw a picture.
* Use a better algorithm or data structure.
* Enable compiler optimizations.
* Tune the code.
* Don't optimize what doesn't matter.
* Collect common subexpressions.
* Replace expensive operations by cheap ones.
* Unroll or eliminate loops.
* Cache frequently-used values.
* Write a special-purpose allocator.
* Buffer input and output.
* Handle special cases separately.
* Precompute results.
* Use approximate values.
* Rewrite in a lower-level language.
* Save space by using the smallest possible data type.
* Don't store what you can easily recompute.

### Portability

* Stick to the standard.
* Program in the mainstream.
* Beware of language trouble spots.
* Try several compilers.
* Use standard libraries.
* Use only features available everywhere.
* Avoid conditional compilation.
* Localize system dependencies in separate files.
* Hide system dependencies behind interfaces.
* Use text for data exchange.
* Use a fixed byte order for data exchange.
* Change the name if you change the specification.
* Maintain compatibility with existing programs and data.
* Don't assume ASCII.
* Don't assume English.

### Xanadu

* Every Xanadu server is uniquely and securely identified.
* Every Xanadu server can be operated independently or in a network.
* Every user is uniquely and securely identified.
* Every user can search, retrieve, create and store documents.
* Every document can consist of any number of parts each of which may be of any
data type.
* Every document can contain links of any type including virtual copies
("transclusions") to any other document in the system accessible to its owner.
* Links are visible and can be followed from all endpoints.
* Permission to link to a document is explicitly granted by the act of
publication.
* Every document can contain a royalty mechanism at any desired degree of
granularity to ensure payment on any portion accessed, including virtual copies
("transclusions") of all or part of the document.
* Every document is uniquely and securely identified.
* Every document can have secure access controls.
* Every document can be rapidly searched, stored and retrieved without user
knowledge of where it is physically stored.
* Every document is automatically moved to physical storage appropriate to its
frequency of access from any given location.
* Every document is automatically stored redundantly to maintain availability
even in case of a disaster.
* Every Xanadu service provider can charge their users at any rate they choose
for the storage, retrieval and publishing of documents.
* Every transaction is secure and auditable only by the parties to that
transaction.
* The Xanadu client-server communication protocol is an openly published
standard. Third-party software development and integration is encouraged.
