;;; Directory Local Variables
;;; For more information see (info "(emacs) Directory Variables")

((js-mode . ((compile-command . "node solve.js")))
 (python-mode . ((compile-command . "python solve.py")))
 (rust-mode . ((compile-command . "rustc solve.rs -o /tmp/solve && /tmp/solve"))))
