

```julia
?open
```

    search: [0m[1mo[22m[0m[1mp[22m[0m[1me[22m[0m[1mn[22m is[0m[1mo[22m[0m[1mp[22m[0m[1me[22m[0m[1mn[22m pr[0m[1mo[22m[0m[1mp[22m[0m[1me[22mrty[0m[1mn[22mames C[0m[1mo[22mm[0m[1mp[22mosit[0m[1me[22mExceptio[0m[1mn[22m [0m[1mo[22m[0m[1mp[22m[0m[1me[22mrm getpr[0m[1mo[22m[0m[1mp[22m[0m[1me[22mrty
    
    




```
open(filename::AbstractString; keywords...) -> IOStream
```

Open a file in a mode specified by five boolean keyword arguments:

| Keyword    | Description            | Default                               |
|:---------- |:---------------------- |:------------------------------------- |
| `read`     | open for reading       | `!write`                              |
| `write`    | open for writing       | `truncate \| append`                  |
| `create`   | create if non-existent | `!read & write \| truncate \| append` |
| `truncate` | truncate to zero size  | `!read & write`                       |
| `append`   | seek to end            | `false`                               |

The default when no keywords are passed is to open files for reading only. Returns a stream for accessing the opened file.

---

```
open(filename::AbstractString, [mode::AbstractString]) -> IOStream
```

Alternate syntax for open, where a string-based mode specifier is used instead of the five booleans. The values of `mode` correspond to those from `fopen(3)` or Perl `open`, and are equivalent to setting the following boolean groups:

| Mode | Description                   | Keywords                       |
|:---- |:----------------------------- |:------------------------------ |
| `r`  | read                          | none                           |
| `w`  | write, create, truncate       | `write = true`                 |
| `a`  | write, create, append         | `append = true`                |
| `r+` | read, write                   | `read = true, write = true`    |
| `w+` | read, write, create, truncate | `truncate = true, read = true` |
| `a+` | read, write, create, append   | `append = true, read = true`   |

# Examples

```jldoctest
julia> io = open("myfile.txt", "w");

julia> write(io, "Hello world!");

julia> close(io);

julia> io = open("myfile.txt", "r");

julia> read(io, String)
"Hello world!"

julia> write(io, "This file is read only")
ERROR: ArgumentError: write failed, IOStream is not writeable
[...]

julia> close(io)

julia> io = open("myfile.txt", "a");

julia> write(io, "This stream is not read only")
28

julia> close(io)

julia> rm("myfile.txt")
```

---

```
open(f::Function, args...; kwargs....)
```

Apply the function `f` to the result of `open(args...; kwargs...)` and close the resulting file descriptor upon completion.

# Examples

```jldoctest
julia> open("myfile.txt", "w") do io
           write(io, "Hello world!")
       end;

julia> open(f->read(f, String), "myfile.txt")
"Hello world!"

julia> rm("myfile.txt")
```

---

```
open(command, stdio=devnull; write::Bool = false, read::Bool = !write)
```

Start running `command` asynchronously, and return a tuple `(stream,process)`.  If `read` is true, then `stream` reads from the process's standard output and `stdio` optionally specifies the process's standard input stream.  If `write` is true, then `stream` writes to the process's standard input and `stdio` optionally specifies the process's standard output stream.

---

```
open(f::Function, command, mode::AbstractString="r", stdio=devnull)
```

Similar to `open(command, mode, stdio)`, but calls `f(stream)` on the resulting process stream, then closes the input stream and waits for the process to complete. Returns the value returned by `f`.





```julia
?readlines
```

    search: [0m[1mr[22m[0m[1me[22m[0m[1ma[22m[0m[1md[22m[0m[1ml[22m[0m[1mi[22m[0m[1mn[22m[0m[1me[22m[0m[1ms[22m [0m[1mr[22m[0m[1me[22m[0m[1ma[22m[0m[1md[22m[0m[1ml[22m[0m[1mi[22m[0m[1mn[22m[0m[1me[22m [0m[1mr[22m[0m[1me[22m[0m[1ma[22m[0m[1md[22m[0m[1ml[22m[0m[1mi[22m[0m[1mn[22mk
    
    




```
readlines(io::IO=stdin; keep::Bool=false)
readlines(filename::AbstractString; keep::Bool=false)
```

Read all lines of an I/O stream or a file as a vector of strings. Behavior is equivalent to saving the result of reading [`readline`](@ref) repeatedly with the same arguments and saving the resulting lines as a vector of strings.

# Examples

```jldoctest
julia> open("my_file.txt", "w") do io
           write(io, "JuliaLang is a GitHub organization.\nIt has many members.\n");
       end
57

julia> readlines("my_file.txt")
2-element Array{String,1}:
 "JuliaLang is a GitHub organization."
 "It has many members."

julia> readlines("my_file.txt", keep=true)
2-element Array{String,1}:
 "JuliaLang is a GitHub organization.\n"
 "It has many members.\n"

julia> rm("my_file.txt")
```





```julia
?readline
```

    search: [0m[1mr[22m[0m[1me[22m[0m[1ma[22m[0m[1md[22m[0m[1ml[22m[0m[1mi[22m[0m[1mn[22m[0m[1me[22m [0m[1mr[22m[0m[1me[22m[0m[1ma[22m[0m[1md[22m[0m[1ml[22m[0m[1mi[22m[0m[1mn[22m[0m[1me[22ms [0m[1mr[22m[0m[1me[22m[0m[1ma[22m[0m[1md[22m[0m[1ml[22m[0m[1mi[22m[0m[1mn[22mk
    
    




```
readline(io::IO=stdin; keep::Bool=false)
readline(filename::AbstractString; keep::Bool=false)
```

Read a single line of text from the given I/O stream or file (defaults to `stdin`). When reading from a file, the text is assumed to be encoded in UTF-8. Lines in the input end with `'\n'` or `"\r\n"` or the end of an input stream. When `keep` is false (as it is by default), these trailing newline characters are removed from the line before it is returned. When `keep` is true, they are returned as part of the line.

# Examples

```jldoctest
julia> open("my_file.txt", "w") do io
           write(io, "JuliaLang is a GitHub organization.\nIt has many members.\n");
       end
57

julia> readline("my_file.txt")
"JuliaLang is a GitHub organization."

julia> readline("my_file.txt", keep=true)
"JuliaLang is a GitHub organization.\n"

julia> rm("my_file.txt")
```





```julia
?split
```

    search: [0m[1ms[22m[0m[1mp[22m[0m[1ml[22m[0m[1mi[22m[0m[1mt[22m [0m[1ms[22m[0m[1mp[22m[0m[1ml[22m[0m[1mi[22m[0m[1mt[22mext [0m[1ms[22m[0m[1mp[22m[0m[1ml[22m[0m[1mi[22m[0m[1mt[22mdir [0m[1ms[22m[0m[1mp[22m[0m[1ml[22m[0m[1mi[22m[0m[1mt[22mdrive r[0m[1ms[22m[0m[1mp[22m[0m[1ml[22m[0m[1mi[22m[0m[1mt[22m [0m[1ms[22m[0m[1mp[22m[0m[1ml[22m[0m[1mi[22mce! di[0m[1ms[22m[0m[1mp[22m[0m[1ml[22mays[0m[1mi[22mze
    
    




```
split(str::AbstractString, dlm; limit::Integer=0, keepempty::Bool=true)
split(str::AbstractString; limit::Integer=0, keepempty::Bool=false)
```

Split `str` into an array of substrings on occurrences of the delimiter(s) `dlm`.  `dlm` can be any of the formats allowed by [`findnext`](@ref)'s first argument (i.e. as a string, regular expression or a function), or as a single character or collection of characters.

If `dlm` is omitted, it defaults to [`isspace`](@ref).

The optional keyword arguments are:

  * `limit`: the maximum size of the result. `limit=0` implies no maximum (default)
  * `keepempty`: whether empty fields should be kept in the result. Default is `false` without a `dlm` argument, `true` with a `dlm` argument.

See also [`rsplit`](@ref).

# Examples

```jldoctest
julia> a = "Ma.rch"
"Ma.rch"

julia> split(a,".")
2-element Array{SubString{String},1}:
 "Ma"
 "rch"
```





```julia
using DelimitedFiles
```


```julia
?DelimitedFiles
```

    search: [0m[1mD[22m[0m[1me[22m[0m[1ml[22m[0m[1mi[22m[0m[1mm[22m[0m[1mi[22m[0m[1mt[22m[0m[1me[22m[0m[1md[22m[0m[1mF[22m[0m[1mi[22m[0m[1ml[22m[0m[1me[22m[0m[1ms[22m
    
    




Utilities for reading and writing delimited files, for example ".csv". See [`readdlm`](@ref) and [`writedlm`](@ref).





```julia
?readdlm
```

    search: [0m[1mr[22m[0m[1me[22m[0m[1ma[22m[0m[1md[22m[0m[1md[22m[0m[1ml[22m[0m[1mm[22m [0m[1mr[22m[0m[1me[22m[0m[1ma[22m[0m[1md[22m[0m[1md[22mir
    
    




```
readdlm(source, T::Type; options...)
```

The columns are assumed to be separated by one or more whitespaces. The end of line delimiter is taken as `\n`.

# Examples

```jldoctest
julia> using DelimitedFiles

julia> x = [1; 2; 3; 4];

julia> y = [5; 6; 7; 8];

julia> open("delim_file.txt", "w") do io
           writedlm(io, [x y])
       end;

julia> readdlm("delim_file.txt", Int64)
4×2 Array{Int64,2}:
 1  5
 2  6
 3  7
 4  8

julia> readdlm("delim_file.txt", Float64)
4×2 Array{Float64,2}:
 1.0  5.0
 2.0  6.0
 3.0  7.0
 4.0  8.0

julia> rm("delim_file.txt")
```

---

```
readdlm(source, delim::AbstractChar, T::Type; options...)
```

The end of line delimiter is taken as `\n`.

# Examples

```jldoctest
julia> using DelimitedFiles

julia> x = [1; 2; 3; 4];

julia> y = [1.1; 2.2; 3.3; 4.4];

julia> open("delim_file.txt", "w") do io
           writedlm(io, [x y], ',')
       end;

julia> readdlm("delim_file.txt", ',', Float64)
4×2 Array{Float64,2}:
 1.0  1.1
 2.0  2.2
 3.0  3.3
 4.0  4.4

julia> rm("delim_file.txt")
```

---

```
readdlm(source; options...)
```

The columns are assumed to be separated by one or more whitespaces. The end of line delimiter is taken as `\n`. If all data is numeric, the result will be a numeric array. If some elements cannot be parsed as numbers, a heterogeneous array of numbers and strings is returned.

# Examples

```jldoctest
julia> using DelimitedFiles

julia> x = [1; 2; 3; 4];

julia> y = ["a"; "b"; "c"; "d"];

julia> open("delim_file.txt", "w") do io
           writedlm(io, [x y])
       end;

julia> readdlm("delim_file.txt")
4×2 Array{Any,2}:
 1  "a"
 2  "b"
 3  "c"
 4  "d"

julia> rm("delim_file.txt")
```

---

```
readdlm(source, delim::AbstractChar; options...)
```

The end of line delimiter is taken as `\n`. If all data is numeric, the result will be a numeric array. If some elements cannot be parsed as numbers, a heterogeneous array of numbers and strings is returned.

# Examples

```jldoctest
julia> using DelimitedFiles

julia> x = [1; 2; 3; 4];

julia> y = [1.1; 2.2; 3.3; 4.4];

julia> open("delim_file.txt", "w") do io
           writedlm(io, [x y], ',')
       end;

julia> readdlm("delim_file.txt", ',')
4×2 Array{Float64,2}:
 1.0  1.1
 2.0  2.2
 3.0  3.3
 4.0  4.4

julia> rm("delim_file.txt")

julia> z = ["a"; "b"; "c"; "d"];

julia> open("delim_file.txt", "w") do io
           writedlm(io, [x z], ',')
       end;

julia> readdlm("delim_file.txt", ',')
4×2 Array{Any,2}:
 1  "a"
 2  "b"
 3  "c"
 4  "d"

julia> rm("delim_file.txt")
```

---

```
readdlm(source, delim::AbstractChar, eol::AbstractChar; options...)
```

If all data is numeric, the result will be a numeric array. If some elements cannot be parsed as numbers, a heterogeneous array of numbers and strings is returned.

---

```
readdlm(source, delim::AbstractChar, T::Type, eol::AbstractChar; header=false, skipstart=0, skipblanks=true, use_mmap, quotes=true, dims, comments=false, comment_char='#')
```

Read a matrix from the source where each line (separated by `eol`) gives one row, with elements separated by the given delimiter. The source can be a text file, stream or byte array. Memory mapped files can be used by passing the byte array representation of the mapped segment as source.

If `T` is a numeric type, the result is an array of that type, with any non-numeric elements as `NaN` for floating-point types, or zero. Other useful values of `T` include `String`, `AbstractString`, and `Any`.

If `header` is `true`, the first row of data will be read as header and the tuple `(data_cells, header_cells)` is returned instead of only `data_cells`.

Specifying `skipstart` will ignore the corresponding number of initial lines from the input.

If `skipblanks` is `true`, blank lines in the input will be ignored.

If `use_mmap` is `true`, the file specified by `source` is memory mapped for potential speedups. Default is `true` except on Windows. On Windows, you may want to specify `true` if the file is large, and is only read once and not written to.

If `quotes` is `true`, columns enclosed within double-quote (") characters are allowed to contain new lines and column delimiters. Double-quote characters within a quoted field must be escaped with another double-quote.  Specifying `dims` as a tuple of the expected rows and columns (including header, if any) may speed up reading of large files.  If `comments` is `true`, lines beginning with `comment_char` and text following `comment_char` in any line are ignored.

# Examples

```jldoctest
julia> using DelimitedFiles

julia> x = [1; 2; 3; 4];

julia> y = [5; 6; 7; 8];

julia> open("delim_file.txt", "w") do io
           writedlm(io, [x y])
       end

julia> readdlm("delim_file.txt", '\t', Int, '\n')
4×2 Array{Int64,2}:
 1  5
 2  6
 3  7
 4  8
```





```julia
?read
```

    search: [0m[1mr[22m[0m[1me[22m[0m[1ma[22m[0m[1md[22m [0m[1mr[22m[0m[1me[22m[0m[1ma[22m[0m[1md[22m! [0m[1mr[22m[0m[1me[22m[0m[1ma[22m[0m[1md[22mdir [0m[1mr[22m[0m[1me[22m[0m[1ma[22m[0m[1md[22mdlm [0m[1mr[22m[0m[1me[22m[0m[1ma[22m[0m[1md[22mlink [0m[1mr[22m[0m[1me[22m[0m[1ma[22m[0m[1md[22mline [0m[1mr[22m[0m[1me[22m[0m[1ma[22m[0m[1md[22muntil [0m[1mr[22m[0m[1me[22m[0m[1ma[22m[0m[1md[22mlines
    
    




```
read(io::IO, T)
```

Read a single value of type `T` from `io`, in canonical binary representation.

```
read(io::IO, String)
```

Read the entirety of `io`, as a `String`.

# Examples

```jldoctest
julia> io = IOBuffer("JuliaLang is a GitHub organization");

julia> read(io, Char)
'J': ASCII/Unicode U+004a (category Lu: Letter, uppercase)

julia> io = IOBuffer("JuliaLang is a GitHub organization");

julia> read(io, String)
"JuliaLang is a GitHub organization"
```

---

```
read(filename::AbstractString, args...)
```

Open a file and read its contents. `args` is passed to `read`: this is equivalent to `open(io->read(io, args...), filename)`.

```
read(filename::AbstractString, String)
```

Read the entire contents of a file as a string.

---

```
read(s::IO, nb=typemax(Int))
```

Read at most `nb` bytes from `s`, returning a `Vector{UInt8}` of the bytes read.

---

```
read(s::IOStream, nb::Integer; all=true)
```

Read at most `nb` bytes from `s`, returning a `Vector{UInt8}` of the bytes read.

If `all` is `true` (the default), this function will block repeatedly trying to read all requested bytes, until an error or end-of-file occurs. If `all` is `false`, at most one `read` call is performed, and the amount of data returned is device-dependent. Note that not all stream types support the `all` option.

---

```
read(command::Cmd)
```

Run `command` and return the resulting output as an array of bytes.

---

```
read(command::Cmd, String)
```

Run `command` and return the resulting output as a `String`.



