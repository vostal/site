var dp = {
    SyntaxHighlighter: {}
};
dp.SyntaxHighlighter = {
    parseParams: function(c, k, l, m, n, o) {
        function d(a, b) {
            return a != null ? a : b
        }

        function f(a) {
            return a != null ? a.toString() : null
        }
        c = c.split(":");
        var g = c[0],
            e = {};
        reverse = {
            "true": false
        };
        result = null;
        defaults = SyntaxHighlighter.defaults;
        for (var j in c) e[c[j]] = "true";
        k = f(d(k, defaults.gutter));
        l = f(d(l, defaults.toolbar));
        m = f(d(m, defaults.collapse));
        o = f(d(o, defaults.ruler));
        n = f(d(n, defaults["first-line"]));
        return {
            brush: g,
            gutter: d(reverse[e.nogutter], k),
            toolbar: d(reverse[e.nocontrols], l),
            collapse: d({
                "true": true
            } [e.collapse], m),
            "first-line": d(function(a, b) {
                for (var h = new XRegExp("^" + b + "\\[(?<value>\\w+)\\]$", "gi"), i = null, p = 0; p < a.length; p++)
                    if ((i = h.exec(a[p])) != null) return i.value;
                return null
            }(c, "firstline"), n)
        }
    },
    HighlightAll: function(c, k, l, m, n, o) {
        function d() {
            for (var a = arguments, b = 0; b < a.length; b++)
                if (a[b] !== null) {
                    if (typeof a[b] == "string" && a[b] != "") return a[b] + "";
                    if (typeof a[b] == "object" && a[b].value != "") return a[b].value + ""
                } return null
        }

        function f(a, b, h) {
            h = document.getElementsByTagName(h);
            for (var i = 0; i < h.length; i++) h[i].getAttribute("name") == b && a.push(h[i])
        }
        var g = [];
        f(g, c, "pre");
        f(g, c, "textarea");
        if (g.length !== 0)
            for (c = 0; c < g.length; c++) {
                var e = g[c],
                    j = d(e.attributes["class"], e.className, e.attributes.language, e.language);
                if (j !== null) {
                    j = dp.SyntaxHighlighter.parseParams(j, k, l, m, n, o);
                    SyntaxHighlighter.highlight(j, e)
                }
            }
    }
};