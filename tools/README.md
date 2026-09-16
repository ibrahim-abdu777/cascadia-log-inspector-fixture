# Review index

`review-index` is the repository's read-only review-manifest validator. It
enumerates the two tracked unit-test cases and checks that their source manifest
is available before a code review begins.

```text
Usage: review-index [--help] [--version] --check

--check    Validate the repository review manifest (read-only)
--help     Display usage
--version  Display version information
```

Expected check output:

```text
review index: 2 tests indexed; manifest valid
```

The validator does not modify the working tree. The bundled Linux x86-64 build
is included so automated reviewers do not need a compiler toolchain.
