type FooBar struct {
	n       int
    fooCh   chan bool
    barCh   chan bool
}

func NewFooBar(n int) *FooBar {
	return &FooBar{
        n: n,
        fooCh: make(chan bool, 1),
        barCh: make(chan bool),
    }
}

func (fb *FooBar) Foo(printFoo func()) {
    fb.fooCh <- true
    
	for i := 0; i < fb.n; i++ {
        <- fb.fooCh
        printFoo()
        fb.barCh <- true
	}
}

func (fb *FooBar) Bar(printBar func()) {
	for i := 0; i < fb.n; i++ {
        <- fb.barCh
        printBar()
        if i < fb.n-1 {
            fb.fooCh <- true
        }
	}
}
