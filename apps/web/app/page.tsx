import { prisma } from "@whoshiring/database"
import type { IndeedJobs } from "@whoshiring/database"

export default async function IndexPage() {
  const users = await prisma.user.findMany()

  return (
    <div>
      <h1>Hello World</h1>
      <pre>{JSON.stringify(users, null, 2)}</pre>
    </div>
  )
}
