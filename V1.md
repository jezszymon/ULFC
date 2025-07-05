# **ULFC 1.0 Documentation**

### Official documentation for ULFC 1.0

## Contents

* [Tools](#tools)
* [Syntax](#syntax)
  * [Source Files](#source-files)
  * [Prefixes](#prefixes)
  * [Characters](#characters)
* [Instruction](#instruction)
  * [Level 0](#level-0)
    * [ADD](#add)
    * [SUB](#sub)
    * [RSH](#rsh)

## **Tools**

> **ULFC Documentation:**
> [https://www.none.com](https://www.none.com)

> **ULFC To ISA:**
> [https://www.none.com](https://www.none.com)

> **ULFC Emulator:**
> [https://www.none.com](https://www.none.com)

## **Syntax**

### **Source Files**

ULFC uses source files with the `.ulfc` extension.

`ULFC source files are utilized within Visual Studio Code. To enhance editing experience, the "ULFC Syntax" extension is available in the VS Code Marketplace, providing syntax highlighting and basic IntelliSense support for ULFC files.`

### **Prefixes**

**Register - `R`**
**Memory - `M`**
**Labels - `.`**
**Comments - `\\`**

### **Characters**

In this assembler, any character specified inside backticks ``''`` is interpreted as its corresponding **7-bit ASCII code**.

For example:

- The notation `` `A` `` represents the ASCII code `65`
- Similarly, `` `0` `` corresponds to ASCII code `48`.

> Note: Only the standard 7-bit ASCII range (0–127) is supported for this notation.

For a comprehensive reference, you can view the full 7-bit ASCII table here: ASCII Table (7-bit)

## **Instruction**
### ADD
#### *Description*
The `ADD` instruction adds the contents of the second and third values and stores the result in the first register.
#### *Operands*
ADD requires 3 operands.

|**Destination**|**Source1**|**Source2**|**Example**|
| :-: | :-: | :-: | :-: |
|Register|Register|Register|<pre>ADD R1 R2 R3</pre>|
|Register|Immediate|Register|<pre>ADD R1 5 R3</pre>|
|Register|Register|Immediate|<pre>ADD R1 R2 7</pre>|
|Register|Immediate|Immediate|<pre>ADD R1 5 7</pre>|

### SUB
#### *Description*
The `SUB` instruction subtracts the third value from the second value and stores the result in the first register.
#### *Operands*
SUB requires 3 operands.

|**Destination**|**Source1**|**Source2**|**Example**|
| :-: | :-: | :-: | :-: |
|Register|Register|Register|<pre>SUB R1 R2 R3</pre>|
|Register|Immediate|Register|<pre>SUB R1 5 R3</pre>|
|Register|Register|Immediate|<pre>SUB R1 R2 7</pre>|
|Register|Immediate|Immediate|<pre>SUB R1 5 7</pre>|

### RSH
#### *Description*
The RSH instruction does a bitwise right shift of a value, then it stores the result in a register.
#### *Operands*
RSH requires 2 operands.

|**Destination**|**Source1**|**Example**|
 :-: | :-: | :-: |
|Register|Register|<pre>RSH R1 R2</pre>|
|Register|Immediate|<pre>RSH R1 5</pre>|