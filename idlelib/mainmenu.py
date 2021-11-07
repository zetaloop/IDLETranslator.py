"""Define the menu contents, hotkeys, and event bindings.

There is additional configuration information in the EditorWindow class (and
subclasses): the menus are created there based on the menu_specs (class)
variable, and menus not created are silently skipped in the code here.  This
makes it possible, for example, to define a Debug menu which is only present in
the PythonShell window, and a Format menu which is only present in the Editor
windows.

"""
from importlib.util import find_spec

from idlelib.config import idleConf

#   Warning: menudefs is altered in macosx.overrideRootMenu()
#   after it is determined that an OS X Aqua Tk is in use,
#   which cannot be done until after Tk() is first called.
#   Do not alter the 'file', 'options', or 'help' cascades here
#   without altering overrideRootMenu() as well.
#       TODO: Make this more robust

menudefs = [
 # underscore prefixes character to underscore
 ('file', [
   ('新建文件(_N)', '<<open-new-window>>'),
   ('打开...(_O)', '<<open-window-from-file>>'),
   ('打开模块...(_M)', '<<open-module>>'),
   ('模块浏览器(_B)', '<<open-class-browser>>'),
   ('路径浏览器(_P)', '<<open-path-browser>>'),
   None,
   ('保存(_S)', '<<save-window>>'),
   ('另存为...(_A)', '<<save-window-as-file>>'),
   ('另存为副本...(_Y)', '<<save-copy-of-window-as-file>>'),
   None,
   ('打印窗口(_T)', '<<print-window>>'),
   None,
   ('关闭(_C)', '<<close-window>>'),
   ('退出(_X)', '<<close-all-windows>>'),
   ]),

 ('edit', [
   ('撤销(_U)', '<<undo>>'),
   ('重做(_R)', '<<redo>>'),
   None,
   ('剪切(_T)', '<<cut>>'),
   ('复制(_C)', '<<copy>>'),
   ('粘贴(_P)', '<<paste>>'),
   ('全选(_A)', '<<select-all>>'),
   None,
   ('查找...(_F)', '<<find>>'),
   ('查找下一个(_G)', '<<find-again>>'),
   ('查找所选文本(_S)', '<<find-selection>>'),
   ('在文件中查找...', '<<find-in-files>>'),
   ('替换...(_E)', '<<replace>>'),
   ('跳转到行(_L)', '<<goto-line>>'),
   ('显示代码提示(_H)', '<<force-open-completions>>'),
   ('自动补全(_X)', '<<expand-word>>'),
   ('显示函数用法提示(_A)', '<<force-open-calltip>>'),
   ('显示括号对(_A)', '<<flash-paren>>'),
   ]),

 ('format', [
   ('格式化段落(_O)', '<<format-paragraph>>'),
   ('缩进(_I)', '<<indent-region>>'),
   ('取消缩进(_D)', '<<dedent-region>>'),
   ('注释(_O)', '<<comment-region>>'),
   ('取消注释(_N)', '<<uncomment-region>>'),
   ('空格转制表符', '<<tabify-region>>'),
   ('制表符转空格', '<<untabify-region>>'),
   ('切换制表符', '<<toggle-tabs>>'),
   ('设置缩进宽度', '<<change-indentwidth>>'),
   ('去除行尾空格(_T)', '<<do-rstrip>>'),
   ]),

 ('run', [
   ('运行代码(_U)', '<<run-module>>'),
   ('自定义运行...(_C)', '<<run-custom>>'),
   ('检查代码(_H)', '<<check-module>>'),
   ('Python 命令行', '<<open-python-shell>>'),
   ]),

 ('shell', [
   ('查看上次重启(_V)', '<<view-restart>>'),
   ('重启命令行(_R)', '<<restart-shell>>'),
   None,
   ('上一条历史记录(_P)', '<<history-previous>>'),
   ('下一条历史记录(_N)', '<<history-next>>'),
   None,
   ('中止执行(_I)', '<<interrupt-execution>>'),
   ]),

 ('debug', [
   ('前往文件/行(_G)', '<<goto-file-line>>'),
   ('!调试器(_D)', '<<toggle-debugger>>'),
   ('堆栈查看器(_S)', '<<open-stack-viewer>>'),
   ('!自动打开堆栈查看器(_A)', '<<toggle-jit-stack-viewer>>'),
   ]),

 ('options', [
   ('IDLE 配置(_I)', '<<open-config-dialog>>'),
   None,
   ('Show _Code Context', '<<toggle-code-context>>'),
   ('Show _Line Numbers', '<<toggle-line-numbers>>'),
   ('_Zoom Height', '<<zoom-height>>'),
   ]),

 ('window', [
   ]),

 ('help', [
   ('关于 IDLE(_A)', '<<about-idle>>'),
   None,
   ('IDLE 帮助(_I)', '<<help>>'),
   ('Python 文档(_D)', '<<python-docs>>'),
   ]),
]

if find_spec('turtledemo'):
    menudefs[-1][1].append(('Turtle 示例程序', '<<open-turtle-demo>>'))

default_keydefs = idleConf.GetCurrentKeySet()

if __name__ == '__main__':
    from unittest import main
    main('idlelib.idle_test.test_mainmenu', verbosity=2)
