(function(){const t=document.createElement("link").relList;if(t&&t.supports&&t.supports("modulepreload"))return;for(const o of document.querySelectorAll('link[rel="modulepreload"]'))l(o);new MutationObserver(o=>{for(const s of o)if(s.type==="childList")for(const d of s.addedNodes)d.tagName==="LINK"&&d.rel==="modulepreload"&&l(d)}).observe(document,{childList:!0,subtree:!0});function n(o){const s={};return o.integrity&&(s.integrity=o.integrity),o.referrerPolicy&&(s.referrerPolicy=o.referrerPolicy),o.crossOrigin==="use-credentials"?s.credentials="include":o.crossOrigin==="anonymous"?s.credentials="omit":s.credentials="same-origin",s}function l(o){if(o.ep)return;o.ep=!0;const s=n(o);fetch(o.href,s)}})();const ie=e=>Array.isArray(e),le=e=>ie(e)?e:[e];let ge=function(e){let t=function(f){return le(f).forEach(E=>{var N;return b.set(Symbol((N=E.char)==null?void 0:N.innerText),o({...E}))}),this},n=()=>p().filter(f=>f.typeable),l=function(f,E){let N=[...b.keys()];b.set(N[f],o(E))},o=f=>(f.shouldPauseCursor=function(){return!!(this.typeable||this.cursorable||this.deletable)},f),s=function(){b.forEach(f=>delete f.done)},d=function(){b=new Map,t(e)},c=()=>b,p=()=>Array.from(b.values()),y=f=>b.delete(f),L=(f=!1)=>f?p():p().filter(E=>!E.done),S=(f,E=!1)=>E?b.delete(f):b.get(f).done=!0,b=new Map;return t(e),{add:t,set:l,wipe:d,reset:s,destroy:y,done:S,getItems:L,getQueue:c,getTypeable:n}};const oe=e=>Array.from(e),W=e=>document.createTextNode(e);let j=e=>([...e.childNodes].forEach(t=>{if(t.nodeValue){[...t.nodeValue].forEach(n=>{t.parentNode.insertBefore(W(n),t)}),t.remove();return}j(t)}),e);const se=e=>{let t=document.implementation.createHTMLDocument();return t.body.innerHTML=e,j(t.body)},ae="data-typeit-id",I="ti-cursor",we="END",Se={started:!1,completed:!1,frozen:!1,destroyed:!1},M={breakLines:!0,cursor:{autoPause:!0,autoPauseDelay:500,animation:{frames:[0,0,1].map(e=>({opacity:e})),options:{iterations:1/0,easing:"steps(2, start)",fill:"forwards"}}},cursorChar:"|",cursorSpeed:1e3,deleteSpeed:null,html:!0,lifeLike:!0,loop:!1,loopDelay:750,nextStringDelay:750,speed:100,startDelay:250,startDelete:!1,strings:[],waitUntilVisible:!1,beforeString:()=>{},afterString:()=>{},beforeStep:()=>{},afterStep:()=>{},afterComplete:()=>{}},Ee=`[${ae}]:before {content: '.'; display: inline-block; width: 0; visibility: hidden;}`;function ue(e,t=!1,n=!1){let l=e.querySelector(`.${I}`),o=document.createTreeWalker(e,NodeFilter.SHOW_ALL,{acceptNode:c=>{var p,y;if(l&&n){if((p=c.classList)!=null&&p.contains(I))return NodeFilter.FILTER_ACCEPT;if(l.contains(c))return NodeFilter.FILTER_REJECT}return(y=c.classList)!=null&&y.contains(I)?NodeFilter.FILTER_REJECT:NodeFilter.FILTER_ACCEPT}}),s,d=[];for(;s=o.nextNode();)s.originalParent||(s.originalParent=s.parentNode),d.push(s);return t?d.reverse():d}function ve(e){return ue(se(e))}function Te(e,t=!0){return t?ve(e):oe(e).map(W)}const H=e=>document.createElement(e),ce=(e,t="")=>{let n=H("style");n.id=t,n.appendChild(W(e)),document.head.appendChild(n)},Z=e=>(ie(e)||(e=[e/2,e/2]),e),ee=(e,t)=>Math.abs(Math.random()*(e+t-(e-t))+(e-t));let te=e=>e/2;function Le(e){let{speed:t,deleteSpeed:n,lifeLike:l}=e;return n=n!==null?n:t/3,l?[ee(t,te(t)),ee(n,te(n))]:[t,n]}const _e=e=>(e.forEach(clearTimeout),[]),Ce=()=>Math.random().toString().substring(2,9),J=e=>"value"in e;let Pe=e=>J(e)?oe(e.value):ue(e,!0).filter(t=>!(t.childNodes.length>0));const Ie=(e,t)=>{new IntersectionObserver((l,o)=>{l.forEach(s=>{s.isIntersecting&&(t(),o.unobserve(e))})},{threshold:1}).observe(e)};let D=e=>typeof e=="function"?e():e;const de=e=>Number.isInteger(e);let K=(e,t=document,n=!1)=>t[`querySelector${n?"All":""}`](e),Ne=e=>/body/i.test(e==null?void 0:e.tagName),Ae=(e,t)=>{if(J(e)){e.value=`${e.value}${t.textContent}`;return}t.innerHTML="";let n=Ne(t.originalParent)?e:t.originalParent||e;n.insertBefore(t,K("."+I,n)||null)},De=(e,t,n)=>Math.min(Math.max(t+e,0),n.length);const x=(e,t)=>Object.assign({},e,t),Me=(e,t)=>{if(!e)return;let n=e.parentNode;(n.childNodes.length>1||n.isSameNode(t)?e:n).remove()},xe=(e,t,n)=>{let l=t[n-1],o=K(`.${I}`,e);e=(l==null?void 0:l.parentNode)||e,e.insertBefore(o,l||null)};function ke(e){return typeof e=="string"?K(e):e}const qe=e=>/<(.+)>(.*?)<\/(.+)>/.test(e.outerHTML);let Fe=(e,t,n)=>new Promise(l=>{let o=async()=>{await e(),l()};n.push(setTimeout(o,t||0))}),Re={"font-family":"","font-weight":"","font-size":"","font-style":"","line-height":"",color:"",transform:"translateX(-.125em)"},He=(e,t)=>{let l=`${`[${ae}='${e}']`} .${I}`,o=getComputedStyle(t),s=Object.entries(Re).reduce((d,[c,p])=>`${d} ${c}: var(--ti-cursor-${c}, ${p||o[c]});`,"");ce(`${l} { display: inline-block; width: 0; ${s} }`,e)};const R=(e,t)=>new Array(t).fill(e),re=({queueItems:e,selector:t,cursorPosition:n,to:l})=>{if(de(t))return t*-1;let o=new RegExp(we,"i").test(l),s=t?[...e].reverse().findIndex(({char:c})=>{let p=c.parentElement,y=p.matches(t);return o&&y?!0:y&&p.firstChild.isSameNode(c)}):-1;s<0&&(s=o?0:e.length-1);let d=o?0:1;return s-n+d};let $=e=>new Promise(t=>{requestAnimationFrame(async()=>{t(await e())})}),fe=e=>e==null?void 0:e.getAnimations().find(t=>t.id===e.dataset.tiAnimationId),me=({cursor:e,frames:t,options:n})=>{let l=e.animate(t,n);return l.pause(),l.id=e.dataset.tiAnimationId,$(()=>{$(()=>{l.play()})}),l},$e=({cursor:e,options:t,cursorOptions:n})=>{if(!e||!n)return;let l=fe(e),o;l&&(t.delay=l.effect.getComputedTiming().delay,o=l.currentTime,l.cancel());let s=me({cursor:e,frames:n.animation.frames,options:t});return o&&(s.currentTime=o),s},ne=e=>{var t;return(t=e.func)==null?void 0:t.call(null)},Qe=async({index:e,queueItems:t,wait:n,cursor:l,cursorOptions:o})=>{let s=t[e][1],d=[],c=e,p=s,y=()=>p&&!p.delay,L=s.shouldPauseCursor()&&o.autoPause;for(;y();)d.push(p),y()&&c++,p=t[c]?t[c][1]:null;if(d.length)return await $(async()=>{for(let f of d)await ne(f)}),c-1;let S=fe(l),b;return S&&(b={...S.effect.getComputedTiming(),delay:L?o.autoPauseDelay:0}),await n(async()=>{S&&L&&S.cancel(),await $(()=>{ne(s)})},s.delay),await $e({cursor:l,options:b,cursorOptions:o}),e},Be=e=>{var t,n;if(typeof e=="object"){let l={},{frames:o,options:s}=M.cursor.animation;return l.animation=e.animation||{},l.animation.frames=((t=e.animation)==null?void 0:t.frames)||o,l.animation.options=x(s,((n=e.animation)==null?void 0:n.options)||{}),l.autoPause=e.autoPause??M.cursor.autoPause,l.autoPauseDelay=e.autoPauseDelay||M.cursor.autoPauseDelay,l}return e===!0?M.cursor:e};const ze=function(e,t={}){let n=async(r,i,u=!1)=>{v.frozen&&await new Promise(m=>{this.unfreeze=()=>{v.frozen=!1,m()}}),u||await a.beforeStep(this),await Fe(r,i,z),u||await a.afterStep(this)},l=(r,i)=>Qe({index:r,queueItems:i,wait:n,cursor:P,cursorOptions:a.cursor}),o=r=>Me(r,h),s=()=>J(h),d=(r=0)=>Le(a)[r],c=()=>Pe(h),p=(r={})=>{let i=r.delay;i&&g.add({delay:i})},y=(r,i)=>(g.add(r),p(i),this),L=()=>G??A,S=(r={})=>[{func:()=>q(r)},{func:()=>q(a)}],b=r=>{let i=a.nextStringDelay;g.add([{delay:i[0]},...r,{delay:i[1]}])},f=()=>{if(s())return;let r=H("span");return r.className=I,Y?(r.innerHTML=se(a.cursorChar).innerHTML,r):(r.style.visibility="hidden",r)},E=async()=>{if(!s()&&P&&h.appendChild(P),Y){He(U,h),P.dataset.tiAnimationId=U;let{animation:r}=a.cursor,{frames:i,options:u}=r;me({frames:i,cursor:P,options:{duration:a.cursorSpeed,...u}})}},N=()=>{let r=a.strings.filter(i=>!!i);r.forEach((i,u)=>{if(this.type(i),u+1===r.length)return;let m=a.breakLines?[{func:()=>B(H("BR")),typeable:!0}]:R({func:F,delay:d(1)},g.getTypeable().length);b(m)})},pe=async r=>{let i=L();i&&await X({value:i});let u=c().map(m=>[Symbol(),{func:F,delay:d(1),deletable:!0,shouldPauseCursor:()=>!0}]);for(let m=0;m<u.length;m++)await l(m,u);g.reset(),g.set(0,{delay:r})},he=r=>{let i=h.innerHTML;return i?(h.innerHTML="",a.startDelete?(h.innerHTML=i,j(h),b(R({func:F,delay:d(1),deletable:!0},c().length)),r):i.replace(/<!--(.+?)-->/g,"").trim().split(/<br(?:\s*?)(?:\/)?>/).concat(r)):r},k=async(r=!0)=>{v.started=!0;let i=u=>{g.done(u,!r)};try{let u=[...g.getQueue()];for(let w=0;w<u.length;w++){let[_,T]=u[w];if(!T.done){if(!T.deletable||T.deletable&&c().length){let C=await l(w,u);Array(C-w).fill(w+1).map((V,O)=>V+O).forEach(V=>{let[O]=u[V];i(O)}),w=C}i(_)}}if(!r)return this;if(v.completed=!0,await a.afterComplete(this),!a.loop)throw"";let m=a.loopDelay;n(async()=>{await pe(m[0]),k()},m[1])}catch{}return this},X=async r=>{A=De(r,A,c()),xe(h,c(),A)},B=r=>Ae(h,r),q=async r=>a=x(a,r),be=async()=>{if(s()){h.value="";return}c().forEach(o)},F=()=>{let r=c();r.length&&(s()?h.value=h.value.slice(0,-1):o(r[A]))};this.break=function(r){return y({func:()=>B(H("BR")),typeable:!0},r)},this.delete=function(r=null,i={}){r=D(r);let u=S(i),m=r,{instant:w,to:_}=i,T=g.getTypeable(),C=(()=>m===null?T.length:de(m)?m:re({queueItems:T,selector:m,cursorPosition:L(),to:_}))();return y([u[0],...R({func:F,delay:w?0:d(1),deletable:!0},C),u[1]],i)},this.empty=function(r={}){return y({func:be},r)},this.exec=function(r,i={}){let u=S(i);return y([u[0],{func:()=>r(this)},u[1]],i)},this.move=function(r,i={}){r=D(r);let u=S(i),{instant:m,to:w}=i,_=re({queueItems:g.getTypeable(),selector:r===null?"":r,to:w,cursorPosition:L()}),T=_<0?-1:1;return G=L()+_,y([u[0],...R({func:()=>X(T),delay:m?0:d(),cursorable:!0},Math.abs(_)),u[1]],i)},this.options=function(r,i={}){return r=D(r),q(r),y({},i)},this.pause=function(r,i={}){return y({delay:D(r)},i)},this.type=function(r,i={}){r=D(r);let{instant:u}=i,m=S(i),_=Te(r,a.html).map(C=>({func:()=>B(C),char:C,delay:u||qe(C)?0:d(),typeable:C.nodeType===Node.TEXT_NODE})),T=[m[0],{func:async()=>await a.beforeString(r,this)},..._,{func:async()=>await a.afterString(r,this)},m[1]];return y(T,i)},this.is=function(r){return v[r]},this.destroy=function(r=!0){z=_e(z),D(r)&&P&&o(P),v.destroyed=!0},this.freeze=function(){v.frozen=!0},this.unfreeze=()=>{},this.reset=function(r){!this.is("destroyed")&&this.destroy(),r?(g.wipe(),r(this)):g.reset(),A=0;for(let i in v)v[i]=!1;return h[s()?"value":"innerHTML"]="",this},this.go=function(){return v.started?this:(E(),a.waitUntilVisible?(Ie(h,k.bind(this)),this):(k(),this))},this.flush=function(r=()=>{}){return E(),k(!1).then(r),this},this.getQueue=()=>g,this.getOptions=()=>a,this.updateOptions=r=>q(r),this.getElement=()=>h;let h=ke(e),z=[],A=0,G=null,v=x({},Se);t.cursor=Be(t.cursor??M.cursor);let a=x(M,t);a=x(a,{html:!s()&&a.html,nextStringDelay:Z(a.nextStringDelay),loopDelay:Z(a.loopDelay)});let U=Ce(),g=ge([{delay:a.startDelay}]);h.dataset.typeitId=U,ce(Ee);let Y=!!a.cursor&&!s(),P=f();a.strings=he(le(a.strings)),a.strings.length&&N()},Ue=document.querySelector(".start_btn-frame");document.addEventListener("DOMContentLoaded",()=>{new ze("#typeItText",{speed:50,waitUntilVisible:!0}).type("Asaalomu",{delay:300}).move(-5).delete(1).type("s").move(null,{to:"END"}).type(" aleykum").pause(300).break().type("<span>Rano-AI</span> ga xush kelibsiz!").pause(700).exec(()=>{Ue.classList.add("active")}).go()});const Ve=document.querySelector(".section-main");Ve.style.height=window.innerHeight+"px";const ye=document.querySelector(".particles");ye.style.width=window.innerWidth+"px";ye.style.height=window.innerHeight+"px";window.addEventListener("resize",e=>{console.log(e.target.screen.availWidth)});const Oe=document.querySelectorAll("header");Oe.forEach(e=>{document.addEventListener("scroll",()=>{window.scrollY===0?e.classList.remove("active"):e.classList.add("active")})});const Q=document.querySelector(".inMobile_nav-frame"),We=document.querySelector(".burger_btn"),je=document.querySelector(".removeMenu_btn");document.body.addEventListener("click",e=>{e.target.classList.contains("inMobile_nav-frame")&&Q.classList.remove("active")});We.addEventListener("click",()=>{Q.classList.add("active")});je.addEventListener("click",()=>{Q.classList.remove("active")});const Je=document.querySelectorAll(".nav-item a");Je.forEach(e=>e.addEventListener("click",()=>{Q.classList.remove("active")}));