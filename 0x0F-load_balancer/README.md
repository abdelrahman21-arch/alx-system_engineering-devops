# 0x0F. Load balancer


## Resource

<details>
<summary>Load balancer</summary><br>
<ul>
  <li>Ever wonder how Facebook, Linkedin, Twitter and other web giants are handling such huge amounts of traffic? They don’t have just one server, but tens of thousands of them. In order to achieve this, web traffic needs to be distributed to these servers, and that is the role of a load-balancer.
</ul>
</details>



<details>
<summary>Web stack debugging</summary><br>
<ul>
  <li>Intro
  <ul>Debugging usually takes a big chunk of a software engineer’s time. The art of debugging is tough and it takes years, even decades to master, and that is why seasoned software engineers are the best at it… experience. They have seen lots of broken code, buggy systems, weird edge cases and race conditions.</ul>
  </li>
</ul>
</details>

[Introduction to load-balancing and HAproxy](https://www.digitalocean.com/community/tutorials/an-introduction-to-haproxy-and-load-balancing-concepts)
- [HAProxy Configuration Basics: Load Balance Your Servers](https://www.haproxy.com/blog/haproxy-configuration-basics-load-balance-your-servers/)
- [The Four Essential Sections of an HAProxy Configuration](https://www.haproxy.com/blog/the-four-essential-sections-of-an-haproxy-configuration/)
- [HTTP Header](https://www.techopedia.com/definition/27178/http-header)
- [Debian/Ubuntu HAProxy packages](https://haproxy.debian.net/)


##Tasks



<details>
<summary><a href="./0-custom_http_response_header">0. Double the number of webservers</a></summary><br>
<a href='https://postimages.org/' target='_blank'><img src='https://i.postimg.cc/prMGd5GF/image.png' border='0' alt='image'/></a>
</details>

<details>
<summary><a href="./1-install_load_balancer">1. Install your load balancer</a></summary><br>
<a href='https://postimages.org/' target='_blank'><img src='https://i.postimg.cc/4dBWZ476/image.png' border='0' alt='image'/></a>
</details>

<details>
<summary><a href="./2-puppet_custom_http_response_header.pp">2. Add a custom HTTP header with Puppet</a></summary><br>
<a href='https://postimages.org/' target='_blank'><img src='https://i.postimg.cc/sD2G5kZY/image.png' border='0' alt='image'/></a>
</details>

