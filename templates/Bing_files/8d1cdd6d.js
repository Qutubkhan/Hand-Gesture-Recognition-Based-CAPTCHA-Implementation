function sj_anim(n){var s=25,t=this,c,u,h,f,e,o,l,i,r;t.init=function(n,s,a,v,y){if(c=n,e=s,o=a,l=v,r=y,v==0){f=h;r&&r();return}i||(i=e);u||t.start()};t.start=function(){h=sb_gt();f=Math.abs(o-i)/l*s;u=setInterval(t.next,s)};t.stop=function(){clearInterval(u);u=0};t.next=function(){var u=sb_gt()-h,s=u>=f;i=e+(o-e)*u/f;s&&(t.stop(),i=o);n(c,i);s&&r&&r()};t.getInterval=function(){return s}}function sj_fader(){return new sj_anim(function(n,t){sj_so(n,t)})}define("shared",["require","exports"],function(n,t){function s(n,t){for(var r=n.length,i=0;i<r;i++)t(n[i])}function r(n){for(var i=[],t=1;t<arguments.length;t++)i[t-1]=arguments[t];return function(){n.apply(null,i)}}function u(n){i&&event&&(event.returnValue=!1);n&&typeof n.preventDefault=="function"&&n.preventDefault()}function f(n){i&&event&&(event.cancelBubble=!0);n&&typeof n.stopPropagation=="function"&&n.stopPropagation()}function e(n,t,i){for(var r=0;n&&n.offsetParent&&n!=(i||document.body);)r+=n["offset"+t],n=n.offsetParent;return r}function o(){return(new Date).getTime()}function h(n){return i?event:n}function c(n){return i?event?event.srcElement:null:n.target}function l(n){return i?event?event.fromElement:null:n.relatedTarget}function a(n){return i?event?event.toElement:null:n.relatedTarget}function v(n,t,i){while(n&&n!=(i||document.body)){if(n==t)return!0;n=n.parentNode}return!1}function y(n){window.location.href=n}function p(n,t){n.style.filter=t>=100?"":"alpha(opacity="+t+")";n.style.opacity=t/100}var i=sb_ie;t.forEach=s;t.wrap=r;t.preventDefault=u;t.stopPropagation=f;t.getOffset=e;t.getTime=o;window.sj_b=document.body;window.sb_de=document.documentElement;window.sj_wf=r;window.sj_pd=u;window.sj_sp=f;window.sj_go=e;window.sj_ev=h;window.sj_et=c;window.sj_mi=l;window.sj_mo=a;window.sj_we=v;window.sb_gt=o;window.sj_so=p;window.sj_lc=y});define("env",["require","exports","shared"],function(n,t,i){function s(n,t){return t.length&&typeof n=="function"?function(){return n.apply(null,t)}:n}function h(n,t){var u=[].slice.apply(arguments).slice(2),i=f(s(n,u),t);return r.push(i),i}function c(n,t){var r=[].slice.apply(arguments).slice(2),i=o(s(n,r),t);return u.push(i),i}function l(){e.forEach(r,window.clearTimeout);e.forEach(u,window.clearInterval);r.length=0;u.length=0}function a(n){window.clearTimeout(n)}var e=i,r=[],u=[],f,o;f=window.setTimeout;t.setTimeout=h;o=window.setInterval;t.setInterval=c;t.clear=l;window.sb_rst=f;window.setTimeout=window.sb_st=h;window.setInterval=window.sb_si=c;window.sb_ct=a});define("event.custom",["require","exports","shared","env"],function(n,t,i,r){function f(n){return u[n]||(u[n]=[])}function e(n,t){n.d?l.setTimeout(c.wrap(n,t),n.d):n(t)}function v(n){for(var t in u)t.indexOf(a)===0||n!=null&&n[t]!=null||delete u[t]}function o(n){for(var t,u,i,o=[],r=0;r<arguments.length-1;r++)o[r]=arguments[r+1];for(t=f(n),u=t.e=arguments,i=0;i<t.length;i++)t[i].alive&&e(t[i].func,u)}function s(n,t,i,r){var u=f(n);t&&(t.d=r,u.push({func:t,alive:!0}),i&&u.e&&e(t,u.e))}function h(n,t){for(var i=0,r=u[n];r&&i<r.length;i++)if(r[i].func==t&&r[i].alive){r[i].alive=!1;break}}var c=i,l=r,u={},a="ajax.";t.reset=v;t.fire=o;t.bind=s;t.unbind=h;_w.sj_evt={bind:s,unbind:h,fire:o}});define("event.native",["require","exports","event.custom"],function(n,t,i){function r(n,t,r,u){var f=n===window||n===document||n===document.body;n&&(f&&t=="load"?i.bind("onP1",r,!0):f&&t=="unload"?i.bind("unload",r,!0):n.addEventListener?n.addEventListener(t,r,u):n.attachEvent?n.attachEvent("on"+t,r):n["on"+t]=r)}function u(n,t,r,u){var f=n===window||n===document||n===document.body;n&&(f&&t=="load"?i.unbind("onP1",r):f&&t=="unload"?i.unbind("unload",r):n.removeEventListener?n.removeEventListener(t,r,u):n.detachEvent?n.detachEvent("on"+t,r):n["on"+t]=null)}t.bind=r;t.unbind=u;window.sj_be=r;window.sj_ue=u});define("onHTML",["require","exports","event.custom"],function(n,t,i){i.fire("onHTML")});define("dom",["require","exports","env","shared","event.native","event.custom"],function(n,t,i,r,u,f){function o(n,t){function c(n,t,i,r){i&&u.unbind(i,r,c);f.bind("onP1",function(){if(!n.l){n.l=1;var i=e("script");i.setAttribute("data-rms","1");i.src=(t?"/fd/sa/"+_G.Ver:"/sa/"+_G.AppVer)+"/"+n.n+".js";_d.body.appendChild(i)}},!0,5)}for(var o=arguments,s,h,i=2,l={n:n};i<o.length;i+=2)s=o[i],h=o[i+1],u.bind(s,h,r.wrap(c,l,t,s,h));i<3&&c(l,t)}function s(){var n=_d.getElementById("ajaxStyles");return n||(n=_d.createElement("div"),n.id="ajaxStyles",_d.body.insertBefore(n,_d.body.firstChild)),n}function l(n){var t=e("script");t.type="text/javascript";t.text=n;t.setAttribute("data-bing-script","1");document.body.appendChild(t);i.setTimeout(function(){document.body.removeChild(t)},0)}function a(n){var t=e("script");t.type="text/javascript";t.src=n;t.onload=i.setTimeout(function(){document.body.removeChild(t)},0);document.body.appendChild(t)}function h(n){var t=c("ajaxStyle");t||(t=e("style"),t.setAttribute("data-rms","1"),t.id="ajaxStyle",s().appendChild(t));t.textContent!==undefined?t.textContent+=n:t.styleSheet.cssText+=n}function c(n){return _d.getElementById(n)}function e(n,t,i){var r=_d.createElement(n);return t&&(r.id=t),i&&(r.className=i),r}t.loadJS=o;t.getCssHolder=s;t.includeScript=l;t.includeScriptReference=a;t.includeCss=h;_w._ge=c;_w.sj_ce=e;_w.sj_jb=o;_w.sj_ic=h});define("cookies",["require","exports"],function(n,t){function r(n,t){var r,u;return i?null:(r=_d.cookie.match(new RegExp("\\b"+n+"=[^;]+")),t&&r)?(u=r[0].match(new RegExp("\\b"+t+"=([^&]*)")),u?u[1]:null):r?r[0]:null}function u(n,t,u,f,e,o){var c,s,h,l;if(!i){s=t+"="+u;h=r(n);h?(l=r(n,t),c=l?h.replace(t+"="+l,s):h+"&"+s):c=n+"="+s;var a=location.hostname.match(/([^.]+\.[^.]*)$/),v=o&&o>0?o*6e4:63072e6,y=new Date((new Date).getTime()+Math.min(v,63072e6));_d.cookie=c+(a?";domain="+a[0]:"")+(f?";expires="+y.toGMTString():"")+(e?";path="+e:"")}}function f(n){if(!i){var r=n+"=",t=location.hostname.match(/([^.]+\.[^.]*)$/);_d.cookie=r+(t?";domain="+t[0]:"")+";expires="+e}}var i=!1,e=new Date(0).toGMTString(),o;try{o=_d.cookie}catch(s){i=!0}t.get=r;t.set=u;t.clear=f;_w.sj_cook={get:r,set:u,clear:f}});define("rmsajax",["require","exports","event.custom"],function(n,t,i){function l(){for(var i,n=[],t=0;t<arguments.length;t++)n[+t]=arguments[t];if(n.length!=0){if(i=n[n.length-1],n.length==1)ot(i)&&f.push(i);else if(n.length==3){var o=n[0],s=n[1],u=n[2];st(o)&&st(s)&&ot(u)&&(ht(r,o,u),ht(e,s,u))}return window.rms}}function nt(){var i=arguments,n,t;for(o.push(i),n=0;n<i.length;n++)t=i[n],ct(t,r),t.d&&tt.call(null,t);return window.rms}function bt(){var t=arguments,n;for(s.push(t),n=0;n<t.length;n++)ct(t[n],e);return window.rms}function a(){var t,i,n;for(ii(),t=!1,n=0;n<o.length;n++)t=tt.apply(null,p.call(o[n],0))||t;for(i=0;i<s.length;i++)t=ni.apply(null,p.call(s[i],0))||t;if(!t)for(n=0;n<f.length;n++)f[n]()}function tt(){var n=arguments,t,i,f,e;if(n.length===0)return!1;if(t=r[ut(n[0])],n.length>1)for(i=ri.apply(null,n),f=0;f<i.length;f++)e=i[f],e.run=u,kt(e,function(n){return function(){dt(n,i)}}(e));else t.run=u,ft(t,function(){it(t)});return!0}function kt(n,t){var r,i;if(!n.state){if(n.state=yt,at(n)){t();return}window.ActiveXObject!==undefined||wt.test(navigator.userAgent)?(r=new Image,r.onload=t,r.onerror=t,r.src=n.url):(i=new XMLHttpRequest,i.open("GET",n.url,!0),i.onreadystatechange=function(){i.readyState==4&&t()},i.send())}}function dt(n,t){n.run==u&&(n.state=w,rt(t))}function gt(n,t){n.run==u&&ft(n,function(n){return function(){it(n,t)}}(n))}function it(n,t){n.run==u&&(n.state=c,ti(n),t)&&rt(t)}function rt(n){for(var i,t=0;t<n.length;t++){i=n[t];switch(i.state){case w:gt(i,n);return;case c:continue}return}}function ut(n){for(var t in n)return t}function ni(){return!1}function ti(n){for(var t=0;t<n.callbacks.length;t++)n.callbacks[t].dec()}function ft(n,t){var i,e,o,u,r;if(n.state!=b&&n.state!=c)if(n.state=b,i=h.createElement("SCRIPT"),i.type="text/javascript",i.setAttribute("data-rms","1"),i.onreadystatechange=i.onload=function(){var n=i.readyState;(!n||/loaded|complete/.test(n))&&et(t)},at(n)){if(e=n.app?d:k,(o=h.getElementById(e))&&(u=o.childNodes)&&u[n.pos]&&(r=u[n.pos].innerHTML,r!=="")){var s=4,l=3,f=r.length,a=r.substring(0,s),v=r.substring(f-l,f);a=="<!--"&&v=="-->"&&(r=r.substring(s,f-l));i.text=r;h.body.appendChild(i)}et(t)}else i.src=n.url,h.body.appendChild(i)}function et(n){n.done||(n.done=!0,n())}function ot(n){return g.call(n)=="[object Function]"}function st(n){return g.call(n)=="[object Array]"}function ht(n,t,i){for(var u,f=new v(i),r=0;r<t.length;r++)u=n[t[r]],u||(u=lt(n,t[r])),y(u,f)}function ii(){for(var t,i,u,n=0;n<f.length;n++){t=new v(f[n]);for(i in r)y(r[i],t);for(u in e)y(e[u],t)}}function y(n,t){n.callbacks.push(t);t.inc()}function ct(n,t){for(var i in n)if(typeof n[i]!=undefined)return lt(t,i,n[i])}function lt(n,t,i){return n[t]||(n[t]={callbacks:[],onPrefetch:[]},n[t].key=t),t.indexOf(pt)==0&&(n[t].app=!0),isNaN(i)?n[t].url=i:n[t].pos=i,n[t]}function ri(){for(var i,t=[],n=0;n<arguments.length;n++)i=ut(arguments[n]),t.push(r[i]);return t}function at(n){return!n.url}function ui(){var n,t;r={};e={};f=[];o=[];s=[];u+=1;n=document.getElementById(k);n&&n.parentNode.removeChild(n);t=document.getElementById(d);t&&t.parentNode.removeChild(t);vt()}function vt(){i.bind("onP1Lazy",function(){l(function(){i.fire("onP1")});a()},!0)}var p=[].slice,yt=1,w=2,b=3,c=4,u=0,pt="A:",k="fRmsDefer",d="aRmsDefer",r={},e={},f=[],o=[],s=[],g=Object.prototype.toString,h=document,wt=/edge/i,v;t.onload=l;t.js=nt;t.css=bt;t.start=a;v=function(n){var t=0,i=!1;this.inc=function(){i||t++};this.dec=function(){i||(t--,t==0&&(i=!0,n()))}};t.reset=ui;vt();window.rms={onload:l,js:nt,start:a}});_w.InstLogQueueKeyFetcher={Get:function(n){var t="eventLogQueue";return n.indexOf("proactive")==1||n.indexOf("search")==1||n.indexOf("zinc")==1?t+"_Online":t+"_Offline"}};define("clientinst",["require","exports","env","event.native","event.custom","shared"],function(n,t,i,r,u,f){function g(n,t,f,o){v||(nt("Init","CI","Base",!1),c=i.setTimeout(e,p),v=1,r.bind(window,"beforeunload",e,!1),u.bind("unload",function(){ot()},!1));nt(n,t,f,o,[].slice.apply(arguments).slice(4))}function nt(n,t,i,r,u){var c="",y,a,v;if(u)for(y=0;y<u.length;y+=2)a=u[y],v=u[y+1],(typeof a!="string"||a[it]('"')<0)&&(a='"'+a+'"'),typeof v!="string"||v.match(ut)||(v='"'+v.replace(rt,'\\"')+'"'),c+=a+":"+v+",";c+='"T":"CI.'+n+'",'+(typeof t=="number"?'"K":'+t:'"FID":"'+t+'"')+',"Name":"'+i+'","TS":'+f.getTime();c=o("{"+c+"}");et[l]+s[l]+c[l]>=ft&&e();s+=o(h?",":"")+c;h=1;r&&e()}function tt(n,t,i,r){var u=n[t];n[t]=function(){var n=arguments,e,t,f;if(r&&i[a](this,n),e=u[a](this,n),!r){for(t=[],f=0;f<n.length;f++)t.push(n[f]);t.push(e);i[a](this,t)}return e}}function ot(){v=0;e()}function e(){c&&clearTimeout(c);h&&(d.src=w+_G.lsUrl+"&TYPE=Event.ClientInst&DATA="+s+o("]"),h=0,s=o("["));c=i.setTimeout(e,p)}var o=encodeURIComponent,l="length",it="indexOf",a="apply",rt=/"/g,ut=/^\s*[{\["].*["}\]]\s*$/g,p=2e3,ft=2e3,s=o("["),h=0,v=0,c,w="",et=_G.lsUrl+"&TYPE=Event.ClientInst&DATA=",b=location.hostname.match(/([^.]+\.[^.]*)$/),y,k,d;b&&(y=location.protocol,k=y=="https:"?"www":"a4",w=y+"//"+k+"."+b[0]);d=new Image;t.Log=g;t.Wrap=tt;window.Log={Log:g,Wrap:tt}});define("replay",["require","exports","fallback"],function(n,t,i){i.replay()});define("framework",["require","exports","event.custom"],function(n,t,i){i.bind("onPP",function(){i.fire("onP1Lazy")},!0)})