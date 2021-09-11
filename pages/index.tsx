import React from 'react';
import type { NextPage } from 'next';
import Head from 'next/head';
import Link from 'next/link';

import Layout, { siteTitle } from '../components/layout';
import Date from '../components/date';

import utilStyles from '../styles/utils.module.scss';

const Home: NextPage = ({ allPostsData }): JSX.Element => {
  return (
    <Layout home>
      <Head>
        <title>{siteTitle}</title>
      </Head>
      <section className={utilStyles.headingMd}>
        <p>
          I'm an enthusiast of web development and SaaS technologies for the supply
          chain. I'm a researcher in operations research and math optimization field. I
          've worked in transportation firms, applying my knowledge in project
          management and programming languages like C++, Python (with Pandas, Numpy and
          Django), SQL and JS (with React and NextJs) to solve problems in processes
          like delivery, routing, location and inventory.
        </p>
        <p>
          (This is a sample website - you’ll be building a site like this on{' '}
          <a href="https://nextjs.org/learn">our Next.js tutorial</a>.)
        </p>
      </section>
      <section className={`${utilStyles.headingMd} ${utilStyles.padding1px}`}>
        <h2 className={utilStyles.headingLg}>Blog</h2>
        <ul className={utilStyles.list}>
          {allPostsData.map(({ id, date, title }) => (
            <li className={utilStyles.listItem} key={id}>
              <Link href={`/posts/${id}`}>{title}</Link>
              <br />
              <small className={utilStyles.lightText}>
                <Date dateString={date} />
              </small>
            </li>
          ))}
        </ul>
      </section>
    </Layout>
  );
};

export default Home;

import { getSortedPostsData } from '../lib/posts';

export async function getStaticProps(): Promise<any> {
  const allPostsData = getSortedPostsData();
  return {
    props: { allPostsData },
  };
}
