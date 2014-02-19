#! /usr/bin/env python
import sys
import argparse
import xml.etree.ElementTree as ET

def itemize_children(node):
	#method to create nested list in Latex
	#check if node is leaf
	if len(node)==0:
		return ''

	#else itemize
	str='\\begin{itemize}\n'
	for child in node:
		str=str+'\item '+child.attrib['TEXT']+'\n'+itemize_children(child)
	return str+'\end{itemize}\n'

def enumerate_children(node):
	#method to create nested list in Latex
	#check if node is leaf
	if len(node)==0:
		return ''

	#else itemize
	str='\\begin{enumerate}\n'
	for child in node:
		str=str+'\item '+child.attrib['TEXT']+'\n'+itemize_children(child)
	return str+'\end{enumerate}\n'

def create_sections(root):
	str=''
	for child in root:
		str=str+'\section*{'+child.attrib['TEXT'] +'}\n'+enumerate_children(child)
	return str

def create_frames(root):
	str=''
	for child in root:
		str=str+'\\begin{frame}{'+child.attrib['TEXT'] +'}\n'+itemize_children(child)+'\n\end{frame}'
	return str

def to_list(tree):
    """ returns the latex-list representation of the tree as string """
    with open('targetTex.tex') as template:
        header = template.read()
    root = tree.getroot()[0]
    title = root.attrib['TEXT']
    header = header.replace("Notes", title)

    return header + create_sections(root) + '\n\end{document}'
   
def to_beamer(tree):
    """ return the beamer-slides representation of the tree as string """
    with open('targetBeamer.tex') as template:
        header = template.read()
    root = tree.getroot()[0]

    return header + create_frames(root) + '\n\end{document}'

if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='texcreator can convert mindmaps\
            to either a latex list or a beamer presentation')
    parser.add_argument('inp', nargs='?', type=argparse.FileType('r'), default=sys.stdin,
            help='input file or stdin')
    parser.add_argument('out', nargs='?', type=argparse.FileType('w'), default=sys.stdout,
            help='output file or stdout')
    parser.add_argument('--to', choices=['list', 'beamer'], default='list',
            help='the desired output format, default: list')
    args = parser.parse_args()
    
    tree = ET.parse(args.inp)
    if args.to == 'list':
        args.out.write(to_list(tree))
    elif args.to == 'beamer':
        args.out.write(to_beamer(tree))
