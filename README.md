# The Pur Project
Pur, the programming language.

Pur is a programming language made in Python. Not assembly because I don't know a single bit of Assembly.

## Documentation

This is the documentation for Pur, because it's probably hard.

### Syntax

The syntax is like this:

```
print.Hi!
print.What's your name?
in.name
printv.name
```

Testing this with the input of hi would result in

```
.Hi!
.What's your name?
hi
hi
```

### Examples
These are for when you're too bored to actually learn, like me.

### 1. Name Repeater

```
print.Hi, what's your name?
in.name
print.Oh,
printv.name
print.cool name! Thanks for tryin'!
```

### 2. Info for No Reason

```
print.Info
print.This is some info for Pur.
print.It was made in Pur, too.
print.Go and watch Nutcracker tho, it's really good
```
### 3. Is It True?

```
in.yes
while.yes
printv.yes
in.yes
end.
```

As there isn't many commands right now, these were the examples.

### Commands
> There may be some non-working commands in this, such as ifvrev.

```
print.{text}
```

```
printv.{var}
```

```
in.{save as var}
```

```
ifvrev.{var}.{val}.{out var}
```

```
error.{error message}
```

```
while.{bool var}
[COMMANDS]
end.
```

```
enable.{library}
```

## Libraries
Style: NAME - DESC - FUNC/DFNC

`git-clone` - Clone using git. - `system(f"git clone {repo}")`

`pypur` - Python in Pur! - Use Python in Pur using PyPur.

## If you're coming from Python
The syntax is different from your usual 2.x or 3.x.

Think of this: `print("Hello!")`

Those () brackets, with the ""?

That would be `print.Hello!`

Saves you a lot of time, don't it? All for a bit of complication.

You might say, "What about `print({var})`?"

That's also here.

It would be `printv.{var}`

`print()` is `print.`

That `v` in `printv.`? That stands for 'var'.

You may also say, "how do we get vars from the user? we have `{var} = input({say string})`

We have that too. It's less stuff, but that'd be `in.{var}`

### While loops

`while True`?

`while True` is `while.True`

`while {user str to bool}`? We try to automatically convert input to what it may be, so conversion is auto, so that'd 

be `while.{uservar}`

The ending for while loops, in Python is an unindent. In Pur, it doesn't use indents. To end a loop in Pur though,

you'd do `end.` That . is just to make it know it's a function.

### If statements

To do `if {var} == {value}`, you would do `ifvrev.{var}.{value}.{out var}`

But the updated `if` will come in soon!

Do what you want with Pur.
Hope you a good line 1!

still water, those who know: